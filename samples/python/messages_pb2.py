# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\rsecondvariety\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\x07\n\x05\x45mpty\"\x86\x05\n\x07GObject\x12\x0b\n\x03Kod\x18\x01 \x01(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x0e\n\x06TekNar\x18\x03 \x01(\x02\x12*\n\x06LastTo\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06ToTime\x18\x05 \x01(\x05\x12\r\n\x05ToNar\x18\x06 \x01(\x02\x12\x10\n\x08PlanYear\x18\x07 \x01(\x02\x12\r\n\x05Koef2\x18\x08 \x01(\x02\x12\r\n\x05Koef1\x18\t \x01(\x02\x12\x0f\n\x07SredNar\x18\n \x01(\x02\x12,\n\x08\x44\x61teFrom\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07NarFrom\x18\x0c \x01(\x02\x12*\n\x06NextTo\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bSredNarPlan\x18\x0e \x01(\x02\x12\x0e\n\x06Status\x18\x0f \x01(\x05\x12\n\n\x02Id\x18\x10 \x01(\x05\x12\x30\n\x0cTrainingFrom\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nTrainingTo\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bWarningType\x18\x13 \x01(\x05\x12/\n\x0bWarningTime\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bWarningFrom\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rWarningSensor\x18\x16 \x01(\x05\x12\x11\n\tErrorRate\x18\x17 \x01(\x02\x12\x13\n\x0b\x45rrorPeriod\x18\x18 \x01(\x05\x12\x10\n\x08HasValue\x18\x19 \x01(\x08\"\x17\n\tGObjectId\x12\n\n\x02Id\x18\x01 \x01(\x05\"\x18\n\nGRequestId\x12\n\n\x02Id\x18\x01 \x01(\x03\"C\n\x08GObjects\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.secondvariety.GObject\x12\x10\n\x08HasValue\x18\x02 \x01(\x08\"t\n\nGNarabotka\x12\x11\n\tKodObject\x18\x01 \x01(\x05\x12(\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03Val\x18\x03 \x01(\x02\x12\n\n\x02Id\x18\x04 \x01(\x05\x12\x10\n\x08HasValue\x18\x05 \x01(\x08\"I\n\x0bGNarabotkas\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.secondvariety.GNarabotka\x12\x10\n\x08HasValue\x18\x02 \x01(\x08\"\xcf\x02\n\x08GRequest\x12\x0b\n\x03Num\x18\x01 \x01(\x05\x12(\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tKodObject\x18\x03 \x01(\x05\x12,\n\x08\x44\x61teFrom\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06\x44\x61teTo\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06Status\x18\x06 \x01(\x05\x12\x30\n\x0c\x44\x61teFromFakt\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nDateToFakt\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x43omment\x18\t \x01(\t\x12\n\n\x02Id\x18\n \x01(\x03\x12\x10\n\x08HasValue\x18\x0b \x01(\x08\"E\n\tGRequests\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.secondvariety.GRequest\x12\x10\n\x08HasValue\x18\x02 \x01(\x08\"\x86\x01\n\nGTelemetry\x12\x0c\n\x04Type\x18\x01 \x01(\x05\x12*\n\x06Period\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05Value\x18\x03 \x01(\x02\x12\n\n\x02Id\x18\x04 \x01(\x05\x12\x11\n\tKodObject\x18\x05 \x01(\x05\x12\x10\n\x08HasValue\x18\x06 \x01(\x08\"I\n\x0bGTelemetrys\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.secondvariety.GTelemetry\x12\x10\n\x08HasValue\x18\x02 \x01(\x08\"x\n\x10GTelemetryPeriod\x12)\n\x05\x42\x65gin\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x45nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08HasValue\x18\x03 \x01(\x08\"\x95\x01\n\x19GTelemetryPeriodForObject\x12+\n\tKodObject\x18\x01 \x01(\x0b\x32\x18.secondvariety.GObjectId\x12\x39\n\x10GTelemetryPeriod\x18\x02 \x01(\x0b\x32\x1f.secondvariety.GTelemetryPeriod\x12\x10\n\x08HasValue\x18\x03 \x01(\x08\"j\n\x12GTelemetryTwoTypes\x12)\n\x05Type1\x18\x01 \x01(\x0b\x32\x1a.secondvariety.GTelemetrys\x12)\n\x05Type2\x18\x02 \x01(\x0b\x32\x1a.secondvariety.GTelemetrys\"\x15\n\x06GClaim\x12\x0b\n\x03Uri\x18\x01 \x01(\t\"\x17\n\x07GWitsml\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c\"0\n\x0cGUploadCount\x12\r\n\x05\x43ount\x18\x01 \x01(\x03\x12\x11\n\tTimeTotal\x18\x02 \x01(\x03\"8\n\x0fGGetTokenClaims\x12%\n\x06\x43laims\x18\x01 \x03(\x0b\x32\x15.secondvariety.GClaim\"\x91\x01\n\x0fGTrainingResult\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x11\n\tKodObject\x18\x02 \x01(\x05\x12\x0e\n\x06MinVal\x18\x03 \x01(\x02\x12\x0e\n\x06MaxVal\x18\x04 \x01(\x02\x12\x0e\n\x06MedVal\x18\x05 \x01(\x02\x12\x0f\n\x07GradVal\x18\x06 \x01(\x02\x12\x0c\n\x04Type\x18\x07 \x01(\x05\x12\x10\n\x08HasValue\x18\x08 \x01(\x08\"S\n\x10GTrainingResults\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.secondvariety.GTrainingResult\x12\x10\n\x08HasValue\x18\x02 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=98
  _EMPTY._serialized_end=105
  _GOBJECT._serialized_start=108
  _GOBJECT._serialized_end=754
  _GOBJECTID._serialized_start=756
  _GOBJECTID._serialized_end=779
  _GREQUESTID._serialized_start=781
  _GREQUESTID._serialized_end=805
  _GOBJECTS._serialized_start=807
  _GOBJECTS._serialized_end=874
  _GNARABOTKA._serialized_start=876
  _GNARABOTKA._serialized_end=992
  _GNARABOTKAS._serialized_start=994
  _GNARABOTKAS._serialized_end=1067
  _GREQUEST._serialized_start=1070
  _GREQUEST._serialized_end=1405
  _GREQUESTS._serialized_start=1407
  _GREQUESTS._serialized_end=1476
  _GTELEMETRY._serialized_start=1479
  _GTELEMETRY._serialized_end=1613
  _GTELEMETRYS._serialized_start=1615
  _GTELEMETRYS._serialized_end=1688
  _GTELEMETRYPERIOD._serialized_start=1690
  _GTELEMETRYPERIOD._serialized_end=1810
  _GTELEMETRYPERIODFOROBJECT._serialized_start=1813
  _GTELEMETRYPERIODFOROBJECT._serialized_end=1962
  _GTELEMETRYTWOTYPES._serialized_start=1964
  _GTELEMETRYTWOTYPES._serialized_end=2070
  _GCLAIM._serialized_start=2072
  _GCLAIM._serialized_end=2093
  _GWITSML._serialized_start=2095
  _GWITSML._serialized_end=2118
  _GUPLOADCOUNT._serialized_start=2120
  _GUPLOADCOUNT._serialized_end=2168
  _GGETTOKENCLAIMS._serialized_start=2170
  _GGETTOKENCLAIMS._serialized_end=2226
  _GTRAININGRESULT._serialized_start=2229
  _GTRAININGRESULT._serialized_end=2374
  _GTRAININGRESULTS._serialized_start=2376
  _GTRAININGRESULTS._serialized_end=2459
# @@protoc_insertion_point(module_scope)
