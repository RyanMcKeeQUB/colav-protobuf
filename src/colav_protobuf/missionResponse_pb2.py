# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: missionResponse.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15missionResponse.proto\x12\x05\x63olav\"\xbf\x02\n\x0fMissionResponse\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12;\n\x08response\x18\x03 \x01(\x0b\x32).colav.MissionResponse.MissionResponseMsg\x1a\xce\x01\n\x12MissionResponseMsg\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.colav.MissionResponse.MissionResponseMsg.ResponseTypeEnum\x12\x0f\n\x07\x64\x65tails\x18\x02 \x01(\t\"]\n\x10ResponseTypeEnum\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10MISSION_STARTING\x10\x01\x12\x11\n\rMISSION_ERROR\x10\x02\x12\x13\n\x0fMISSION_INVALID\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'missionResponse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MISSIONRESPONSE']._serialized_start=33
  _globals['_MISSIONRESPONSE']._serialized_end=352
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEMSG']._serialized_start=146
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEMSG']._serialized_end=352
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEMSG_RESPONSETYPEENUM']._serialized_start=259
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEMSG_RESPONSETYPEENUM']._serialized_end=352
# @@protoc_insertion_point(module_scope)
