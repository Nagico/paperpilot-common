import abc
import collections.abc
import typing

import grpc
import grpc.aio

_T = typing.TypeVar("_T")


class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    pass


class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):
    pass
