# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='service/followers/definition/followers.proto',
  package='bnet.protocol.followers',
  serialized_pb='\n,service/followers/definition/followers.proto\x12\x17\x62net.protocol.followers\x1a\x1clib/protocol/attribute.proto\x1a\x19lib/protocol/entity.proto\x1a\x11lib/rpc/rpc.proto\"j\n\x0c\x46ollowedUser\x12#\n\x02id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x02 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"[\n\x1bSubscribeToFollowersRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x02(\x04\"]\n\x1cSubscribeToFollowersResponse\x12=\n\x0e\x66ollowed_users\x18\x02 \x03(\x0b\x32%.bnet.protocol.followers.FollowedUser\"\x85\x01\n\x15StartFollowingRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x15\n\rfollower_name\x18\x03 \x01(\t\"V\n\x16StartFollowingResponse\x12<\n\rfollowed_user\x18\x02 \x01(\x0b\x32%.bnet.protocol.followers.FollowedUser\"m\n\x14StopFollowingRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"U\n\x15StopFollowingResponse\x12<\n\rfollowed_user\x18\x02 \x01(\x0b\x32%.bnet.protocol.followers.FollowedUser\"\xaa\x01\n\x1aUpdateFollowerStateRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"\x80\x01\n\x1bUpdateFollowerStateResponse\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"T\n\x14\x46ollowerNotification\x12<\n\rfollowed_user\x18\x01 \x02(\x0b\x32%.bnet.protocol.followers.FollowedUser2\xfe\x03\n\x10\x46ollowersService\x12\x83\x01\n\x14SubscribeToFollowers\x12\x34.bnet.protocol.followers.SubscribeToFollowersRequest\x1a\x35.bnet.protocol.followers.SubscribeToFollowersResponse\x12q\n\x0eStartFollowing\x12..bnet.protocol.followers.StartFollowingRequest\x1a/.bnet.protocol.followers.StartFollowingResponse\x12n\n\rStopFollowing\x12-.bnet.protocol.followers.StopFollowingRequest\x1a..bnet.protocol.followers.StopFollowingResponse\x12\x80\x01\n\x13UpdateFollowerState\x12\x33.bnet.protocol.followers.UpdateFollowerStateRequest\x1a\x34.bnet.protocol.followers.UpdateFollowerStateResponse2u\n\x0f\x46ollowersNotify\x12\x62\n\x15NotifyFollowerRemoved\x12-.bnet.protocol.followers.FollowerNotification\x1a\x1a.bnet.protocol.NO_RESPONSEB\x03\x80\x01\x01')




_FOLLOWEDUSER = descriptor.Descriptor(
  name='FollowedUser',
  full_name='bnet.protocol.followers.FollowedUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.followers.FollowedUser.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.followers.FollowedUser.attribute', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=149,
  serialized_end=255,
)


_SUBSCRIBETOFOLLOWERSREQUEST = descriptor.Descriptor(
  name='SubscribeToFollowersRequest',
  full_name='bnet.protocol.followers.SubscribeToFollowersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.followers.SubscribeToFollowersRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.followers.SubscribeToFollowersRequest.object_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=257,
  serialized_end=348,
)


_SUBSCRIBETOFOLLOWERSRESPONSE = descriptor.Descriptor(
  name='SubscribeToFollowersResponse',
  full_name='bnet.protocol.followers.SubscribeToFollowersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='followed_users', full_name='bnet.protocol.followers.SubscribeToFollowersResponse.followed_users', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=350,
  serialized_end=443,
)


_STARTFOLLOWINGREQUEST = descriptor.Descriptor(
  name='StartFollowingRequest',
  full_name='bnet.protocol.followers.StartFollowingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.followers.StartFollowingRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.followers.StartFollowingRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='follower_name', full_name='bnet.protocol.followers.StartFollowingRequest.follower_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=446,
  serialized_end=579,
)


_STARTFOLLOWINGRESPONSE = descriptor.Descriptor(
  name='StartFollowingResponse',
  full_name='bnet.protocol.followers.StartFollowingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='followed_user', full_name='bnet.protocol.followers.StartFollowingResponse.followed_user', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=581,
  serialized_end=667,
)


_STOPFOLLOWINGREQUEST = descriptor.Descriptor(
  name='StopFollowingRequest',
  full_name='bnet.protocol.followers.StopFollowingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.followers.StopFollowingRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.followers.StopFollowingRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=669,
  serialized_end=778,
)


_STOPFOLLOWINGRESPONSE = descriptor.Descriptor(
  name='StopFollowingResponse',
  full_name='bnet.protocol.followers.StopFollowingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='followed_user', full_name='bnet.protocol.followers.StopFollowingResponse.followed_user', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=780,
  serialized_end=865,
)


_UPDATEFOLLOWERSTATEREQUEST = descriptor.Descriptor(
  name='UpdateFollowerStateRequest',
  full_name='bnet.protocol.followers.UpdateFollowerStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.followers.UpdateFollowerStateRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.followers.UpdateFollowerStateRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.followers.UpdateFollowerStateRequest.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=868,
  serialized_end=1038,
)


_UPDATEFOLLOWERSTATERESPONSE = descriptor.Descriptor(
  name='UpdateFollowerStateResponse',
  full_name='bnet.protocol.followers.UpdateFollowerStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.followers.UpdateFollowerStateResponse.target_id', index=0,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.followers.UpdateFollowerStateResponse.attribute', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1041,
  serialized_end=1169,
)


_FOLLOWERNOTIFICATION = descriptor.Descriptor(
  name='FollowerNotification',
  full_name='bnet.protocol.followers.FollowerNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='followed_user', full_name='bnet.protocol.followers.FollowerNotification.followed_user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1171,
  serialized_end=1255,
)

import lib.protocol.attribute_pb2
import lib.protocol.entity_pb2
import lib.rpc.rpc_pb2

_FOLLOWEDUSER.fields_by_name['id'].message_type = lib.protocol.entity_pb2._ENTITYID
_FOLLOWEDUSER.fields_by_name['attribute'].message_type = lib.protocol.attribute_pb2._ATTRIBUTE
_SUBSCRIBETOFOLLOWERSREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUBSCRIBETOFOLLOWERSRESPONSE.fields_by_name['followed_users'].message_type = _FOLLOWEDUSER
_STARTFOLLOWINGREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_STARTFOLLOWINGREQUEST.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_STARTFOLLOWINGRESPONSE.fields_by_name['followed_user'].message_type = _FOLLOWEDUSER
_STOPFOLLOWINGREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_STOPFOLLOWINGREQUEST.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_STOPFOLLOWINGRESPONSE.fields_by_name['followed_user'].message_type = _FOLLOWEDUSER
_UPDATEFOLLOWERSTATEREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_UPDATEFOLLOWERSTATEREQUEST.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_UPDATEFOLLOWERSTATEREQUEST.fields_by_name['attribute'].message_type = lib.protocol.attribute_pb2._ATTRIBUTE
_UPDATEFOLLOWERSTATERESPONSE.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_UPDATEFOLLOWERSTATERESPONSE.fields_by_name['attribute'].message_type = lib.protocol.attribute_pb2._ATTRIBUTE
_FOLLOWERNOTIFICATION.fields_by_name['followed_user'].message_type = _FOLLOWEDUSER

class FollowedUser(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOLLOWEDUSER
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.FollowedUser)

class SubscribeToFollowersRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSCRIBETOFOLLOWERSREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.SubscribeToFollowersRequest)

class SubscribeToFollowersResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSCRIBETOFOLLOWERSRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.SubscribeToFollowersResponse)

class StartFollowingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTFOLLOWINGREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.StartFollowingRequest)

class StartFollowingResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTFOLLOWINGRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.StartFollowingResponse)

class StopFollowingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPFOLLOWINGREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.StopFollowingRequest)

class StopFollowingResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPFOLLOWINGRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.StopFollowingResponse)

class UpdateFollowerStateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEFOLLOWERSTATEREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.UpdateFollowerStateRequest)

class UpdateFollowerStateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEFOLLOWERSTATERESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.UpdateFollowerStateResponse)

class FollowerNotification(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOLLOWERNOTIFICATION
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.followers.FollowerNotification)


_FOLLOWERSSERVICE = descriptor.ServiceDescriptor(
  name='FollowersService',
  full_name='bnet.protocol.followers.FollowersService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1258,
  serialized_end=1768,
  methods=[
  descriptor.MethodDescriptor(
    name='SubscribeToFollowers',
    full_name='bnet.protocol.followers.FollowersService.SubscribeToFollowers',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBETOFOLLOWERSREQUEST,
    output_type=_SUBSCRIBETOFOLLOWERSRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='StartFollowing',
    full_name='bnet.protocol.followers.FollowersService.StartFollowing',
    index=1,
    containing_service=None,
    input_type=_STARTFOLLOWINGREQUEST,
    output_type=_STARTFOLLOWINGRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='StopFollowing',
    full_name='bnet.protocol.followers.FollowersService.StopFollowing',
    index=2,
    containing_service=None,
    input_type=_STOPFOLLOWINGREQUEST,
    output_type=_STOPFOLLOWINGRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='UpdateFollowerState',
    full_name='bnet.protocol.followers.FollowersService.UpdateFollowerState',
    index=3,
    containing_service=None,
    input_type=_UPDATEFOLLOWERSTATEREQUEST,
    output_type=_UPDATEFOLLOWERSTATERESPONSE,
    options=None,
  ),
])

class FollowersService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _FOLLOWERSSERVICE
class FollowersService_Stub(FollowersService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _FOLLOWERSSERVICE


_FOLLOWERSNOTIFY = descriptor.ServiceDescriptor(
  name='FollowersNotify',
  full_name='bnet.protocol.followers.FollowersNotify',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1770,
  serialized_end=1887,
  methods=[
  descriptor.MethodDescriptor(
    name='NotifyFollowerRemoved',
    full_name='bnet.protocol.followers.FollowersNotify.NotifyFollowerRemoved',
    index=0,
    containing_service=None,
    input_type=_FOLLOWERNOTIFICATION,
    output_type=lib.rpc.rpc_pb2._NO_RESPONSE,
    options=None,
  ),
])

class FollowersNotify(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _FOLLOWERSNOTIFY
class FollowersNotify_Stub(FollowersNotify):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _FOLLOWERSNOTIFY

# @@protoc_insertion_point(module_scope)