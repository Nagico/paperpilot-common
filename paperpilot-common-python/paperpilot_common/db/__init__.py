import signal
import sys

from tortoise import Tortoise, run_async

from paperpilot_common.conf import settings


def tortoise_init():
    run_async(__init())
    register_tortoise_shutdown()


def __get_conf():
    from paperpilot_common.apps import apps

    connections = settings.DATABASES

    apps_conf = {}

    for app_name, app_config in apps.app_configs.items():
        apps_conf[app_name] = {"models": [f"{app_name}.models"], "default_connection": "default"}

    conf = {
        "connections": connections,
        "apps": apps,
    }
    return conf


async def __init():
    conf = __get_conf()

    # support default db only
    await Tortoise.init(
        config=conf,
        use_tz=settings.USE_TZ,
        timezone=settings.TIME_ZONE,
    )


def register_tortoise_shutdown():
    for signame in [x for x in dir(signal) if x.startswith("SIG")]:
        try:
            signum = getattr(signal, signame)
            signal.signal(signum, __shutdown_handler)
        except (OSError, RuntimeError, ValueError):
            pass


def __shutdown_handler(signum, _):
    run_async(Tortoise.close_connections())
    sys.exit(signum)
