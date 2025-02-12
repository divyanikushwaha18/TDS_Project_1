import os
import json
from ..config import settings
from .llm_service import LLMService
from .file_service import FileService

class TaskHandler:
    def __init__(self, token: str):
        self.llm = LLMService(token)
        self.file_service = FileService()

    async def process_task(self, task_description: str):
        # Task classification using LLM
        task_type = await self.llm.classify_task(task_description)
        
        # Execute task based on classification
        if task_type == "format_markdown":
            return await self.file_service.format_markdown(task_description)
        # Add more task handlers
        
        raise ValueError("Unsupported task type")

    async def read_file(self, path: str):
        return await self.file_service.read_file(path)
    