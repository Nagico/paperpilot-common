# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from paperpilot_common.protobuf.ai import ai_pb2 as paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2


class GptServiceStub(object):
    """GPT 服务"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ask = channel.unary_stream(
            "/ai.GptService/Ask",
            request_serializer=paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptRequest.SerializeToString,
            response_deserializer=paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptResult.FromString,
        )


class GptServiceServicer(object):
    """GPT 服务"""

    def Ask(self, request, context):
        """询问 GPT"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GptServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ask": grpc.unary_stream_rpc_method_handler(
            servicer.Ask,
            request_deserializer=paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptRequest.FromString,
            response_serializer=paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptResult.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("ai.GptService", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class GptService(object):
    """GPT 服务"""

    @staticmethod
    def Ask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/ai.GptService/Ask",
            paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptRequest.SerializeToString,
            paperpilot__common_dot_protobuf_dot_ai_dot_ai__pb2.GptResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )