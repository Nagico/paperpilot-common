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
class IMAuthResponse(google.protobuf.message.Message):
    """IM认证响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    id: builtins.str
    """user id"""
    sig: builtins.str
    """user sig"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        sig: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "sig", b"sig"]) -> None: ...

global___IMAuthResponse = IMAuthResponse

@typing_extensions.final
class CreateUserRequest(google.protobuf.message.Message):
    """新建用户请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    id: builtins.str
    """用户id"""
    username: builtins.str
    """用户名"""
    avatar: builtins.str
    """用户头像"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        username: builtins.str = ...,
        avatar: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["avatar", b"avatar", "id", b"id", "username", b"username"]
    ) -> None: ...

global___CreateUserRequest = CreateUserRequest

@typing_extensions.final
class UpdateUserRequest(google.protobuf.message.Message):
    """更新用户请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    id: builtins.str
    """用户id"""
    username: builtins.str
    """用户名"""
    avatar: builtins.str
    """用户头像"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        username: builtins.str = ...,
        avatar: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["avatar", b"avatar", "id", b"id", "username", b"username"]
    ) -> None: ...

global___UpdateUserRequest = UpdateUserRequest

@typing_extensions.final
class CreateWorkGroupRequest(google.protobuf.message.Message):
    """创建Work群组请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    id: builtins.str
    """群组id"""
    name: builtins.str
    """群组名称"""
    owner: builtins.str
    """群主id"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        owner: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "owner", b"owner"]
    ) -> None: ...

global___CreateWorkGroupRequest = CreateWorkGroupRequest

@typing_extensions.final
class UpdateWorkGroupRequest(google.protobuf.message.Message):
    """更新Work群组请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """群组id"""
    name: builtins.str
    """群组名称"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name"]) -> None: ...

global___UpdateWorkGroupRequest = UpdateWorkGroupRequest

@typing_extensions.final
class DeleteWorkGroupRequest(google.protobuf.message.Message):
    """删除Work群组请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """群组id"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___DeleteWorkGroupRequest = DeleteWorkGroupRequest

@typing_extensions.final
class InviteUserToGroupRequest(google.protobuf.message.Message):
    """邀请用户加入群组请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    group_id: builtins.str
    """群组id"""
    user_id: builtins.str
    """用户id"""
    def __init__(
        self,
        *,
        group_id: builtins.str = ...,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["group_id", b"group_id", "user_id", b"user_id"]
    ) -> None: ...

global___InviteUserToGroupRequest = InviteUserToGroupRequest

@typing_extensions.final
class RemoveUserFromGroupRequest(google.protobuf.message.Message):
    """从群组中移除用户请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    group_id: builtins.str
    """群组id"""
    user_id: builtins.str
    """用户id"""
    def __init__(
        self,
        *,
        group_id: builtins.str = ...,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["group_id", b"group_id", "user_id", b"user_id"]
    ) -> None: ...

global___RemoveUserFromGroupRequest = RemoveUserFromGroupRequest