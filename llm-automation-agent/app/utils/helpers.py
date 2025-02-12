import os
from pathlib import Path
from typing import List
from app import settings

def ensure_data_dir_path(path: str) -> str:
    """Ensure path is within data directory"""
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(settings.DATA_DIR):
        raise ValueError("Path must be within data directory")
    return abs_path

def list_files(directory: str, pattern: str) -> List[str]:
    """List files matching pattern in directory"""
    path = Path(directory)
    return [str(p) for p in path.glob(pattern)]
