import sys
from pathlib import Path


def get_existed_file_path(path: str) -> Path | None:
    if path is None:
        return None

    path = Path(path)

    # 如果路径是绝对路径并且存在，则返回 Path 对象
    if path.is_absolute() and path.exists():
        return path

    # 获取sys.path中的路径列表
    for search_path in sys.path:
        current_path = Path(search_path) / path
        if current_path.exists():
            return current_path

        # 如果未找到文件或路径不存在，则返回 None
    return None
