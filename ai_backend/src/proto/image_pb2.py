# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bimage.proto\x12\x12\x63om.ssafy.pjt.grpc\"X\n\x11OriginalImageInfo\x12\x15\n\roriginalImage\x18\x01 \x01(\x0c\x12,\n\x07options\x18\x02 \x01(\x0b\x32\x1b.com.ssafy.pjt.grpc.Options\"\x9d\x01\n\x12ProcessedImageInfo\x12\x16\n\x0eprocessedImage\x18\x01 \x01(\x0c\x12\x34\n\x0bresponseUrl\x18\x02 \x01(\x0b\x32\x1f.com.ssafy.pjt.grpc.ResponseUrl\x12\x39\n\x06result\x18\x03 \x01(\x0e\x32).com.ssafy.pjt.grpc.ImageProcessingResult\"_\n\x07Options\x12\x12\n\nbackground\x18\x01 \x01(\t\x12\x0c\n\x04suit\x18\x02 \x01(\t\x12\x0c\n\x04hair\x18\x03 \x01(\t\x12$\n\x03sex\x18\x04 \x01(\x0e\x32\x17.com.ssafy.pjt.grpc.SEX\"]\n\x0bResponseUrl\x12\x18\n\x10originalImageUrl\x18\x01 \x01(\t\x12\x19\n\x11processedImageUrl\x18\x02 \x01(\t\x12\x19\n\x11thumbnailImageUrl\x18\x03 \x01(\t*\x1b\n\x03SEX\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01*@\n\x15ImageProcessingResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07NO_FACE\x10\x01\x12\r\n\tMANY_FACE\x10\x02\x32i\n\x0b\x43reateImage\x12Z\n\tsendImage\x12%.com.ssafy.pjt.grpc.OriginalImageInfo\x1a&.com.ssafy.pjt.grpc.ProcessedImageInfob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SEX']._serialized_start=477
  _globals['_SEX']._serialized_end=504
  _globals['_IMAGEPROCESSINGRESULT']._serialized_start=506
  _globals['_IMAGEPROCESSINGRESULT']._serialized_end=570
  _globals['_ORIGINALIMAGEINFO']._serialized_start=35
  _globals['_ORIGINALIMAGEINFO']._serialized_end=123
  _globals['_PROCESSEDIMAGEINFO']._serialized_start=126
  _globals['_PROCESSEDIMAGEINFO']._serialized_end=283
  _globals['_OPTIONS']._serialized_start=285
  _globals['_OPTIONS']._serialized_end=380
  _globals['_RESPONSEURL']._serialized_start=382
  _globals['_RESPONSEURL']._serialized_end=475
  _globals['_CREATEIMAGE']._serialized_start=572
  _globals['_CREATEIMAGE']._serialized_end=677
# @@protoc_insertion_point(module_scope)