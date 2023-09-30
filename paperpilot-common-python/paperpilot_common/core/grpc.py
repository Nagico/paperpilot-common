import paperpilot_common
from paperpilot_common.core.handlers.grpc import GrpcHandler


def get_grpc_application():
    """
    The public interface to Django's ASGI support. Return an ASGI 3 callable.

    Avoids making django.core.handlers.ASGIHandler a public API, in case the
    internal implementation changes or moves in the future.
    """
    paperpilot_common.setup()
    return GrpcHandler()
