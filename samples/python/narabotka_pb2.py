# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: narabotka.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
import messages_pb2 as messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fnarabotka.proto\x12\rsecondvariety\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x0emessages.proto2\x88\x03\n\rNarabotkaServ\x12:\n\x06GetAll\x12\x14.secondvariety.Empty\x1a\x1a.secondvariety.GNarabotkas\x12>\n\x07GetById\x12\x18.secondvariety.GObjectId\x1a\x19.secondvariety.GNarabotka\x12\x46\n\x0eGetByObjectKod\x12\x18.secondvariety.GObjectId\x1a\x1a.secondvariety.GNarabotkas\x12<\n\x04Post\x12\x19.secondvariety.GNarabotka\x1a\x19.secondvariety.GNarabotka\x12;\n\x03Put\x12\x19.secondvariety.GNarabotka\x1a\x19.secondvariety.GNarabotka\x12\x38\n\x06\x44\x65lete\x12\x18.secondvariety.GObjectId\x1a\x14.secondvariety.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'narabotka_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NARABOTKASERV._serialized_start=116
  _NARABOTKASERV._serialized_end=508
# @@protoc_insertion_point(module_scope)
