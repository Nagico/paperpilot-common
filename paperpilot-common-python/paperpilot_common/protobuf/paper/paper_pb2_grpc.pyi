"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import paperpilot_common.protobuf.paper.paper_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class PaperServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    AddPaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """添加论文"""
    UpdatePaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """更新论文"""

class PaperServiceAsyncStub:
    AddPaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """添加论文"""
    UpdatePaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """更新论文"""

class PaperServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def AddPaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """添加论文"""
    @abc.abstractmethod
    def UpdatePaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """更新论文"""

def add_PaperServiceServicer_to_server(
    servicer: PaperServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]
) -> None: ...

class PaperPublicServiceStub:
    """论文公开接口"""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ListPaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.ListPaperRequest,
        paperpilot_common.protobuf.paper.paper_pb2.ListPaperResponse,
    ]
    """获取论文列表"""
    GetPaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """获取论文详情"""
    CreatePaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.CreatePaperRequest,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """添加论文"""
    CreatePaperByLink: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.CreatePaperByLinkRequest,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """从链接创建论文"""
    UpdatePaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """更新论文"""
    UploadAttachment: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentRequest,
        paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentResponse,
    ]
    """上传附件"""
    DeletePaper: grpc.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        google.protobuf.empty_pb2.Empty,
    ]
    """删除论文"""

class PaperPublicServiceAsyncStub:
    """论文公开接口"""

    ListPaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.ListPaperRequest,
        paperpilot_common.protobuf.paper.paper_pb2.ListPaperResponse,
    ]
    """获取论文列表"""
    GetPaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """获取论文详情"""
    CreatePaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.CreatePaperRequest,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """添加论文"""
    CreatePaperByLink: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.CreatePaperByLinkRequest,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """从链接创建论文"""
    UpdatePaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
    ]
    """更新论文"""
    UploadAttachment: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentRequest,
        paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentResponse,
    ]
    """上传附件"""
    DeletePaper: grpc.aio.UnaryUnaryMultiCallable[
        paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        google.protobuf.empty_pb2.Empty,
    ]
    """删除论文"""

class PaperPublicServiceServicer(metaclass=abc.ABCMeta):
    """论文公开接口"""

    @abc.abstractmethod
    def ListPaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.ListPaperRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.ListPaperResponse,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.ListPaperResponse],
    ]:
        """获取论文列表"""
    @abc.abstractmethod
    def GetPaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """获取论文详情"""
    @abc.abstractmethod
    def CreatePaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.CreatePaperRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """添加论文"""
    @abc.abstractmethod
    def CreatePaperByLink(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.CreatePaperByLinkRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """从链接创建论文"""
    @abc.abstractmethod
    def UpdatePaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.PaperDetail,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.PaperDetail],
    ]:
        """更新论文"""
    @abc.abstractmethod
    def UploadAttachment(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentResponse,
        collections.abc.Awaitable[paperpilot_common.protobuf.paper.paper_pb2.UploadAttachmentResponse],
    ]:
        """上传附件"""
    @abc.abstractmethod
    def DeletePaper(
        self,
        request: paperpilot_common.protobuf.paper.paper_pb2.PaperId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]:
        """删除论文"""

def add_PaperPublicServiceServicer_to_server(
    servicer: PaperPublicServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]
) -> None: ...
