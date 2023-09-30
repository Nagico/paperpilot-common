import grpc.aio
from asgiref.sync import ThreadSensitiveContext

from paperpilot_common.conf import settings
from paperpilot_common.middleware.server.base import AsyncServerMiddleware
from paperpilot_common.utils.log import get_logger
from paperpilot_common.utils.module_loading import import_string

logger = get_logger("server.request")


class GrpcHandler:
    """Handler for gRPC requests."""

    middleware_list: list[AsyncServerMiddleware]

    def __init__(self):
        super().__init__()
        self.load_middleware()

    async def __call__(self, scope, receive, send):
        """
        Async entrypoint - parses the request and hands off to get_response.
        """
        # Serve only HTTP connections.
        # FIXME: Allow to override this.
        if scope["type"] != "http":
            raise ValueError("Django can only handle ASGI/HTTP connections, not %s." % scope["type"])

        async with ThreadSensitiveContext():
            await self.handle(scope, receive, send)

    def load_middleware(self):
        self.middleware_list = []

        for middleware_path in settings.MIDDLEWARE:
            middleware = import_string(middleware_path)

            self.middleware_list.append(middleware())

    def bind_apps(self, server: grpc.aio.Server):
        from paperpilot_common.apps import apps

        count = 0

        for name, app in apps.app_configs.items():
            count += 1
            logger.debug(f"Binding app: {name}")
            app.bind(server)

        logger.info(f"{count} app(s) bound.")
