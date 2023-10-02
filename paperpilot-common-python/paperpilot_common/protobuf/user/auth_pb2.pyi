"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import paperpilot_common.protobuf.user.user_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class LoginRequest(google.protobuf.message.Message):
    """登录请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PHONE_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    phone: builtins.str
    """手机号"""
    password: builtins.str
    """密码"""
    def __init__(
        self,
        *,
        phone: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password", b"password", "phone", b"phone"]) -> None: ...

global___LoginRequest = LoginRequest

@typing_extensions.final
class Token(google.protobuf.message.Message):
    """token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    EXPIRE_TIME_FIELD_NUMBER: builtins.int
    value: builtins.str
    """token值"""
    @property
    def expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """过期时间"""
    def __init__(
        self,
        *,
        value: builtins.str = ...,
        expire_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expire_time", b"expire_time"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["expire_time", b"expire_time", "value", b"value"]
    ) -> None: ...

global___Token = Token

@typing_extensions.final
class LoginResponse(google.protobuf.message.Message):
    """登录响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    REFRESH_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> paperpilot_common.protobuf.user.user_pb2.UserInfo:
        """用户信息"""
    @property
    def access(self) -> global___Token:
        """access token"""
    @property
    def refresh(self) -> global___Token:
        """refresh token"""
    def __init__(
        self,
        *,
        user: paperpilot_common.protobuf.user.user_pb2.UserInfo | None = ...,
        access: global___Token | None = ...,
        refresh: global___Token | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["access", b"access", "refresh", b"refresh", "user", b"user"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["access", b"access", "refresh", b"refresh", "user", b"user"]
    ) -> None: ...

global___LoginResponse = LoginResponse

@typing_extensions.final
class RefreshTokenRequest(google.protobuf.message.Message):
    """刷新token请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REFRESH_FIELD_NUMBER: builtins.int
    refresh: builtins.str
    """refresh token"""
    def __init__(
        self,
        *,
        refresh: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["refresh", b"refresh"]) -> None: ...

global___RefreshTokenRequest = RefreshTokenRequest

@typing_extensions.final
class RefreshTokenResponse(google.protobuf.message.Message):
    """刷新token响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_FIELD_NUMBER: builtins.int
    @property
    def access(self) -> global___Token:
        """access token"""
    def __init__(
        self,
        *,
        access: global___Token | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["access", b"access"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access", b"access"]) -> None: ...

global___RefreshTokenResponse = RefreshTokenResponse

@typing_extensions.final
class SendSmsCodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PHONE_FIELD_NUMBER: builtins.int
    phone: builtins.str
    """手机号"""
    def __init__(
        self,
        *,
        phone: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["phone", b"phone"]) -> None: ...

global___SendSmsCodeRequest = SendSmsCodeRequest
