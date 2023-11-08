# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: paperpilot_common/protobuf/paper/paper.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

from paperpilot_common.protobuf.common import util_pb2 as paperpilot__common_dot_protobuf_dot_common_dot_util__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,paperpilot_common/protobuf/paper/paper.proto\x12\x05paper\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a,paperpilot_common/protobuf/common/util.proto"\x15\n\x07PaperId\x12\n\n\x02id\x18\x01 \x01(\t"\xf5\x02\n\x0bPaperDetail\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08\x61\x62stract\x18\x04 \x01(\t\x12\x10\n\x08keywords\x18\x05 \x03(\t\x12\x0f\n\x07\x61uthors\x18\x06 \x03(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x18\n\x10publication_year\x18\x08 \x01(\x05\x12\x13\n\x0bpublication\x18\t \x01(\t\x12\x0e\n\x06volume\x18\n \x01(\t\x12\r\n\x05issue\x18\x0b \x01(\t\x12\r\n\x05pages\x18\x0c \x01(\t\x12\x0b\n\x03url\x18\r \x01(\t\x12\x0b\n\x03\x64oi\x18\x0e \x01(\t\x12\x0c\n\x04\x66ile\x18\x0f \x01(\t\x12/\n\x0b\x63reate_time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x65vent\x18\x12 \x01(\t"Y\n\x10ListPaperRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x10\n\x08order_by\x18\x04 \x01(\t"Y\n\x11ListPaperResponse\x12"\n\x06papers\x18\x01 \x03(\x0b\x32\x12.paper.PaperDetail\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x11\n\tnext_page\x18\x03 \x01(\x05"K\n\x12\x43reatePaperRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12!\n\x05paper\x18\x02 \x01(\x0b\x32\x12.paper.PaperDetail"Q\n\x17UpdateAttachmentRequest\x12\x10\n\x08paper_id\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\x12\x16\n\x0e\x66\x65tch_metadata\x18\x03 \x01(\x08"C\n\x17UploadAttachmentRequest\x12\x10\n\x08paper_id\x18\x01 \x01(\t\x12\x16\n\x0e\x66\x65tch_metadata\x18\x02 \x01(\x08"9\n\x18UploadAttachmentResponse\x12\x1d\n\x05token\x18\x01 \x01(\x0b\x32\x0e.util.OssToken"<\n\x18\x43reatePaperByLinkRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t2\xc1\x01\n\x0cPaperService\x12\x32\n\x08\x41\x64\x64Paper\x12\x12.paper.PaperDetail\x1a\x12.paper.PaperDetail\x12\x35\n\x0bUpdatePaper\x12\x12.paper.PaperDetail\x1a\x12.paper.PaperDetail\x12\x46\n\x10UpdateAttachment\x12\x1e.paper.UpdateAttachmentRequest\x1a\x12.paper.PaperDetail2\xcf\x03\n\x12PaperPublicService\x12>\n\tListPaper\x12\x17.paper.ListPaperRequest\x1a\x18.paper.ListPaperResponse\x12.\n\x08GetPaper\x12\x0e.paper.PaperId\x1a\x12.paper.PaperDetail\x12<\n\x0b\x43reatePaper\x12\x19.paper.CreatePaperRequest\x1a\x12.paper.PaperDetail\x12H\n\x11\x43reatePaperByLink\x12\x1f.paper.CreatePaperByLinkRequest\x1a\x12.paper.PaperDetail\x12\x35\n\x0bUpdatePaper\x12\x12.paper.PaperDetail\x1a\x12.paper.PaperDetail\x12S\n\x10UploadAttachment\x12\x1e.paper.UploadAttachmentRequest\x1a\x1f.paper.UploadAttachmentResponse\x12\x35\n\x0b\x44\x65letePaper\x12\x0e.paper.PaperId\x1a\x16.google.protobuf.Emptyb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "paperpilot_common.protobuf.paper.paper_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_PAPERID"]._serialized_start = 195
    _globals["_PAPERID"]._serialized_end = 216
    _globals["_PAPERDETAIL"]._serialized_start = 219
    _globals["_PAPERDETAIL"]._serialized_end = 592
    _globals["_LISTPAPERREQUEST"]._serialized_start = 594
    _globals["_LISTPAPERREQUEST"]._serialized_end = 683
    _globals["_LISTPAPERRESPONSE"]._serialized_start = 685
    _globals["_LISTPAPERRESPONSE"]._serialized_end = 774
    _globals["_CREATEPAPERREQUEST"]._serialized_start = 776
    _globals["_CREATEPAPERREQUEST"]._serialized_end = 851
    _globals["_UPDATEATTACHMENTREQUEST"]._serialized_start = 853
    _globals["_UPDATEATTACHMENTREQUEST"]._serialized_end = 934
    _globals["_UPLOADATTACHMENTREQUEST"]._serialized_start = 936
    _globals["_UPLOADATTACHMENTREQUEST"]._serialized_end = 1003
    _globals["_UPLOADATTACHMENTRESPONSE"]._serialized_start = 1005
    _globals["_UPLOADATTACHMENTRESPONSE"]._serialized_end = 1062
    _globals["_CREATEPAPERBYLINKREQUEST"]._serialized_start = 1064
    _globals["_CREATEPAPERBYLINKREQUEST"]._serialized_end = 1124
    _globals["_PAPERSERVICE"]._serialized_start = 1127
    _globals["_PAPERSERVICE"]._serialized_end = 1320
    _globals["_PAPERPUBLICSERVICE"]._serialized_start = 1323
    _globals["_PAPERPUBLICSERVICE"]._serialized_end = 1786
# @@protoc_insertion_point(module_scope)
