import os
import json
from pathlib import Path
from ..config import settings

class FileService:
    async def read_file(self, path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    async def write_file(self, path: str, content: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)

    async def format_markdown(self, file_path: str) -> None:
        # Implementation for prettier formatting
        pass
    