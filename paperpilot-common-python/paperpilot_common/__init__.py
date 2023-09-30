from paperpilot_common.utils.version import get_version

VERSION = (0, 0, 9, "alpha", 0)

__version__ = get_version(VERSION)


def setup():
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from paperpilot_common.apps import apps
    from paperpilot_common.conf import settings
    from paperpilot_common.utils.log import configure_logging

    configure_logging(fmt=settings.LOG_FMT, level=settings.LOG_LEVEL)
    apps.populate(settings.INSTALLED_APPS)
