# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class GGetTokensServStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetToken = channel.unary_unary(
                '/secondvariety.GGetTokensServ/GetToken',
                request_serializer=messages__pb2.GGetTokenClaims.SerializeToString,
                response_deserializer=messages__pb2.GClaim.FromString,
                )


class GGetTokensServServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GGetTokensServServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetToken,
                    request_deserializer=messages__pb2.GGetTokenClaims.FromString,
                    response_serializer=messages__pb2.GClaim.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'secondvariety.GGetTokensServ', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GGetTokensServ(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.GGetTokensServ/GetToken',
            messages__pb2.GGetTokenClaims.SerializeToString,
            messages__pb2.GClaim.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
