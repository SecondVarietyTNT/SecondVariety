# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class ObjectsServStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAll = channel.unary_unary(
                '/secondvariety.ObjectsServ/GetAll',
                request_serializer=messages__pb2.Empty.SerializeToString,
                response_deserializer=messages__pb2.GObjects.FromString,
                )
        self.GetById = channel.unary_unary(
                '/secondvariety.ObjectsServ/GetById',
                request_serializer=messages__pb2.GObjectId.SerializeToString,
                response_deserializer=messages__pb2.GObject.FromString,
                )
        self.Post = channel.unary_unary(
                '/secondvariety.ObjectsServ/Post',
                request_serializer=messages__pb2.GObject.SerializeToString,
                response_deserializer=messages__pb2.GObject.FromString,
                )
        self.Put = channel.unary_unary(
                '/secondvariety.ObjectsServ/Put',
                request_serializer=messages__pb2.GObject.SerializeToString,
                response_deserializer=messages__pb2.GObject.FromString,
                )
        self.Delete = channel.unary_unary(
                '/secondvariety.ObjectsServ/Delete',
                request_serializer=messages__pb2.GObjectId.SerializeToString,
                response_deserializer=messages__pb2.Empty.FromString,
                )


class ObjectsServServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Post(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Put(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectsServServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=messages__pb2.Empty.FromString,
                    response_serializer=messages__pb2.GObjects.SerializeToString,
            ),
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=messages__pb2.GObjectId.FromString,
                    response_serializer=messages__pb2.GObject.SerializeToString,
            ),
            'Post': grpc.unary_unary_rpc_method_handler(
                    servicer.Post,
                    request_deserializer=messages__pb2.GObject.FromString,
                    response_serializer=messages__pb2.GObject.SerializeToString,
            ),
            'Put': grpc.unary_unary_rpc_method_handler(
                    servicer.Put,
                    request_deserializer=messages__pb2.GObject.FromString,
                    response_serializer=messages__pb2.GObject.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=messages__pb2.GObjectId.FromString,
                    response_serializer=messages__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'secondvariety.ObjectsServ', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObjectsServ(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.ObjectsServ/GetAll',
            messages__pb2.Empty.SerializeToString,
            messages__pb2.GObjects.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.ObjectsServ/GetById',
            messages__pb2.GObjectId.SerializeToString,
            messages__pb2.GObject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Post(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.ObjectsServ/Post',
            messages__pb2.GObject.SerializeToString,
            messages__pb2.GObject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.ObjectsServ/Put',
            messages__pb2.GObject.SerializeToString,
            messages__pb2.GObject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.ObjectsServ/Delete',
            messages__pb2.GObjectId.SerializeToString,
            messages__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
