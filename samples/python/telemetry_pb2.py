# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry.proto
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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftelemetry.proto\x12\rsecondvariety\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x0emessages.proto\x1a\x1bgoogle/protobuf/empty.proto2\xfa\x06\n\rTelemetryServ\x12\x44\n\nGetForDate\x12\x1a.google.protobuf.Timestamp\x1a\x1a.secondvariety.GTelemetrys\x12>\n\x07GetById\x12\x18.secondvariety.GObjectId\x1a\x19.secondvariety.GTelemetry\x12K\n\x0cGetForPeriod\x12\x1f.secondvariety.GTelemetryPeriod\x1a\x1a.secondvariety.GTelemetrys\x12\x62\n\x1aGetForPeriodForObjectByKod\x12(.secondvariety.GTelemetryPeriodForObject\x1a\x1a.secondvariety.GTelemetrys\x12l\n\x1dGetForPeriodForObjectWarning4\x12(.secondvariety.GTelemetryPeriodForObject\x1a!.secondvariety.GTelemetryTwoTypes\x12G\n\x13GetLastTrainedRecId\x12\x16.google.protobuf.Empty\x1a\x18.secondvariety.GObjectId\x12=\n\x0bTrainingObj\x12\x18.secondvariety.GObjectId\x1a\x14.secondvariety.Empty\x12H\n\x0fUploadTelemetry\x12\x16.secondvariety.GWitsml\x1a\x1b.secondvariety.GUploadCount(\x01\x12=\n\x0b\x43heckingObj\x12\x18.secondvariety.GObjectId\x1a\x14.secondvariety.Empty\x12<\n\x04Post\x12\x19.secondvariety.GTelemetry\x1a\x19.secondvariety.GTelemetry\x12;\n\x03Put\x12\x19.secondvariety.GTelemetry\x1a\x19.secondvariety.GTelemetry\x12\x38\n\x06\x44\x65lete\x12\x18.secondvariety.GObjectId\x1a\x14.secondvariety.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'telemetry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TELEMETRYSERV._serialized_start=145
  _TELEMETRYSERV._serialized_end=1035
# @@protoc_insertion_point(module_scope)
