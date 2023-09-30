import warnings

from paperpilot_common.conf import DEFAULT_STORAGE_ALIAS, settings
from paperpilot_common.utils.deprecation import RemovedInPaperpilot51Warning
from paperpilot_common.utils.functional import LazyObject
from paperpilot_common.utils.module_loading import import_string

from .base import Storage
from .filesystem import FileSystemStorage
from .handler import InvalidStorageError, StorageHandler
from .memory import InMemoryStorage

__all__ = (
    "FileSystemStorage",
    "InMemoryStorage",
    "Storage",
    "DefaultStorage",
    "default_storage",
    "get_storage_class",
    "InvalidStorageError",
    "StorageHandler",
    "storages",
)

GET_STORAGE_CLASS_DEPRECATED_MSG = (
    "paperpilot_common.core.files.storage.get_storage_class is deprecated in favor of "
    "using paperpilot_common.core.files.storage.storages."
)


def get_storage_class(import_path=None):
    warnings.warn(GET_STORAGE_CLASS_DEPRECATED_MSG, RemovedInPaperpilot51Warning)
    return import_string(import_path or settings.DEFAULT_FILE_STORAGE)


class DefaultStorage(LazyObject):
    def _setup(self):
        self._wrapped = storages[DEFAULT_STORAGE_ALIAS]


storages = StorageHandler()
default_storage = DefaultStorage()
