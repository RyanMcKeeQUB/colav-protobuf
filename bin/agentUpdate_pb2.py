# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agentUpdate.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agentUpdate.proto',
  package='colav',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x61gentUpdate.proto\x12\x05\x63olav\"\xcc\x03\n\x0b\x41gentUpdate\x12\x13\n\x0bmission_tag\x18\x01 \x02(\t\x12\x11\n\tagent_tag\x18\x02 \x02(\t\x12\'\n\x05state\x18\x03 \x02(\x0b\x32\x18.colav.AgentUpdate.State\x12\x11\n\ttimestamp\x18\x04 \x02(\t\x12\x10\n\x08timestep\x18\x05 \x02(\t\x1a\xdc\x01\n\x04Pose\x12\x32\n\x08position\x18\x01 \x02(\x0b\x32 .colav.AgentUpdate.Pose.Position\x12\x38\n\x0borientation\x18\x02 \x02(\x0b\x32#.colav.AgentUpdate.Pose.Orientation\x1a+\n\x08Position\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\x1a\x39\n\x0bOrientation\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\x12\t\n\x01w\x18\x04 \x02(\x02\x1ah\n\x05State\x12%\n\x04pose\x18\x01 \x02(\x0b\x32\x17.colav.AgentUpdate.Pose\x12\x10\n\x08velocity\x18\x02 \x02(\x02\x12\x10\n\x08yaw_rate\x18\x03 \x02(\x02\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x04 \x02(\x02'
)




_AGENTUPDATE_POSE_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='colav.AgentUpdate.Pose.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='colav.AgentUpdate.Pose.Position.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='colav.AgentUpdate.Pose.Position.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='colav.AgentUpdate.Pose.Position.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=324,
)

_AGENTUPDATE_POSE_ORIENTATION = _descriptor.Descriptor(
  name='Orientation',
  full_name='colav.AgentUpdate.Pose.Orientation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='colav.AgentUpdate.Pose.Orientation.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='colav.AgentUpdate.Pose.Orientation.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='colav.AgentUpdate.Pose.Orientation.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='colav.AgentUpdate.Pose.Orientation.w', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=383,
)

_AGENTUPDATE_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='colav.AgentUpdate.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='colav.AgentUpdate.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='colav.AgentUpdate.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_AGENTUPDATE_POSE_POSITION, _AGENTUPDATE_POSE_ORIENTATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=383,
)

_AGENTUPDATE_STATE = _descriptor.Descriptor(
  name='State',
  full_name='colav.AgentUpdate.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='colav.AgentUpdate.State.pose', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='colav.AgentUpdate.State.velocity', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_rate', full_name='colav.AgentUpdate.State.yaw_rate', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='colav.AgentUpdate.State.acceleration', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=489,
)

_AGENTUPDATE = _descriptor.Descriptor(
  name='AgentUpdate',
  full_name='colav.AgentUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission_tag', full_name='colav.AgentUpdate.mission_tag', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_tag', full_name='colav.AgentUpdate.agent_tag', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='colav.AgentUpdate.state', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='colav.AgentUpdate.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestep', full_name='colav.AgentUpdate.timestep', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_AGENTUPDATE_POSE, _AGENTUPDATE_STATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=489,
)

_AGENTUPDATE_POSE_POSITION.containing_type = _AGENTUPDATE_POSE
_AGENTUPDATE_POSE_ORIENTATION.containing_type = _AGENTUPDATE_POSE
_AGENTUPDATE_POSE.fields_by_name['position'].message_type = _AGENTUPDATE_POSE_POSITION
_AGENTUPDATE_POSE.fields_by_name['orientation'].message_type = _AGENTUPDATE_POSE_ORIENTATION
_AGENTUPDATE_POSE.containing_type = _AGENTUPDATE
_AGENTUPDATE_STATE.fields_by_name['pose'].message_type = _AGENTUPDATE_POSE
_AGENTUPDATE_STATE.containing_type = _AGENTUPDATE
_AGENTUPDATE.fields_by_name['state'].message_type = _AGENTUPDATE_STATE
DESCRIPTOR.message_types_by_name['AgentUpdate'] = _AGENTUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentUpdate = _reflection.GeneratedProtocolMessageType('AgentUpdate', (_message.Message,), {

  'Pose' : _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {

    'Position' : _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
      'DESCRIPTOR' : _AGENTUPDATE_POSE_POSITION,
      '__module__' : 'agentUpdate_pb2'
      # @@protoc_insertion_point(class_scope:colav.AgentUpdate.Pose.Position)
      })
    ,

    'Orientation' : _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), {
      'DESCRIPTOR' : _AGENTUPDATE_POSE_ORIENTATION,
      '__module__' : 'agentUpdate_pb2'
      # @@protoc_insertion_point(class_scope:colav.AgentUpdate.Pose.Orientation)
      })
    ,
    'DESCRIPTOR' : _AGENTUPDATE_POSE,
    '__module__' : 'agentUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.AgentUpdate.Pose)
    })
  ,

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR' : _AGENTUPDATE_STATE,
    '__module__' : 'agentUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.AgentUpdate.State)
    })
  ,
  'DESCRIPTOR' : _AGENTUPDATE,
  '__module__' : 'agentUpdate_pb2'
  # @@protoc_insertion_point(class_scope:colav.AgentUpdate)
  })
_sym_db.RegisterMessage(AgentUpdate)
_sym_db.RegisterMessage(AgentUpdate.Pose)
_sym_db.RegisterMessage(AgentUpdate.Pose.Position)
_sym_db.RegisterMessage(AgentUpdate.Pose.Orientation)
_sym_db.RegisterMessage(AgentUpdate.State)


# @@protoc_insertion_point(module_scope)
