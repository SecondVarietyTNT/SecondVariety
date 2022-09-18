# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class NarabotkaServStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAll = channel.unary_unary(
                '/secondvariety.NarabotkaServ/GetAll',
                request_serializer=messages__pb2.Empty.SerializeToString,
                response_deserializer=messages__pb2.GNarabotkas.FromString,
                )
        self.GetById = channel.unary_unary(
                '/secondvariety.NarabotkaServ/GetById',
                request_serializer=messages__pb2.GObjectId.SerializeToString,
                response_deserializer=messages__pb2.GNarabotka.FromString,
                )
        self.GetByObjectKod = channel.unary_unary(
                '/secondvariety.NarabotkaServ/GetByObjectKod',
                request_serializer=messages__pb2.GObjectId.SerializeToString,
                response_deserializer=messages__pb2.GNarabotkas.FromString,
                )
        self.Post = channel.unary_unary(
                '/secondvariety.NarabotkaServ/Post',
                request_serializer=messages__pb2.GNarabotka.SerializeToString,
                response_deserializer=messages__pb2.GNarabotka.FromString,
                )
        self.Put = channel.unary_unary(
                '/secondvariety.NarabotkaServ/Put',
                request_serializer=messages__pb2.GNarabotka.SerializeToString,
                response_deserializer=messages__pb2.GNarabotka.FromString,
                )
        self.Delete = channel.unary_unary(
                '/secondvariety.NarabotkaServ/Delete',
                request_serializer=messages__pb2.GObjectId.SerializeToString,
                response_deserializer=messages__pb2.Empty.FromString,
                )


class NarabotkaServServicer(object):
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

    def GetByObjectKod(self, request, context):
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


def add_NarabotkaServServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=messages__pb2.Empty.FromString,
                    response_serializer=messages__pb2.GNarabotkas.SerializeToString,
            ),
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=messages__pb2.GObjectId.FromString,
                    response_serializer=messages__pb2.GNarabotka.SerializeToString,
            ),
            'GetByObjectKod': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByObjectKod,
                    request_deserializer=messages__pb2.GObjectId.FromString,
                    response_serializer=messages__pb2.GNarabotkas.SerializeToString,
            ),
            'Post': grpc.unary_unary_rpc_method_handler(
                    servicer.Post,
                    request_deserializer=messages__pb2.GNarabotka.FromString,
                    response_serializer=messages__pb2.GNarabotka.SerializeToString,
            ),
            'Put': grpc.unary_unary_rpc_method_handler(
                    servicer.Put,
                    request_deserializer=messages__pb2.GNarabotka.FromString,
                    response_serializer=messages__pb2.GNarabotka.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=messages__pb2.GObjectId.FromString,
                    response_serializer=messages__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'secondvariety.NarabotkaServ', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NarabotkaServ(object):
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
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/GetAll',
            messages__pb2.Empty.SerializeToString,
            messages__pb2.GNarabotkas.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/GetById',
            messages__pb2.GObjectId.SerializeToString,
            messages__pb2.GNarabotka.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByObjectKod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/GetByObjectKod',
            messages__pb2.GObjectId.SerializeToString,
            messages__pb2.GNarabotkas.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/Post',
            messages__pb2.GNarabotka.SerializeToString,
            messages__pb2.GNarabotka.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/Put',
            messages__pb2.GNarabotka.SerializeToString,
            messages__pb2.GNarabotka.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/secondvariety.NarabotkaServ/Delete',
            messages__pb2.GObjectId.SerializeToString,
            messages__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)