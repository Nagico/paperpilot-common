"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Date(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    YEAR_FIELD_NUMBER: builtins.int
    MONTH_FIELD_NUMBER: builtins.int
    DAY_FIELD_NUMBER: builtins.int
    year: builtins.int
    month: builtins.int
    day: builtins.int
    def __init__(
        self,
        *,
        year: builtins.int = ...,
        month: builtins.int = ...,
        day: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["day", b"day", "month", b"month", "year", b"year"]
    ) -> None: ...

global___Date = Date

@typing_extensions.final
class OssToken(google.protobuf.message.Message):
    """Oss直传Token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    CALLBACK_HOST_FIELD_NUMBER: builtins.int
    CALLBACK_BODY_FIELD_NUMBER: builtins.int
    access_key_id: builtins.str
    """oss access key id"""
    policy: builtins.str
    """上传参数"""
    signature: builtins.str
    """签名"""
    callback_host: builtins.str
    """回调地址"""
    callback_body: builtins.str
    """回调参数"""
    def __init__(
        self,
        *,
        access_key_id: builtins.str = ...,
        policy: builtins.str = ...,
        signature: builtins.str = ...,
        callback_host: builtins.str = ...,
        callback_body: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "access_key_id",
            b"access_key_id",
            "callback_body",
            b"callback_body",
            "callback_host",
            b"callback_host",
            "policy",
            b"policy",
            "signature",
            b"signature",
        ],
    ) -> None: ...

global___OssToken = OssToken
