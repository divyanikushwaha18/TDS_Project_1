import pytest
from app.services.task_handler import TaskHandler
from app.config import settings

@pytest.fixture
def task_handler():
    return TaskHandler(settings.AIPROXY_TOKEN)

@pytest.mark.asyncio
async def test_format_markdown(task_handler):
    task = "Format /data/format.md using prettier"
    result = await task_handler.process_task(task)
    assert result is not None

@pytest.mark.asyncio
async def test_count_wednesdays(task_handler):
    task = "Count Wednesdays in /data/dates.txt"
    result = await task_handler.process_task(task)
    assert isinstance(result, dict)
    assert "count" in result

@pytest.mark.asyncio
async def test_sort_contacts(task_handler):
    task = "Sort contacts in /data/contacts.json"
    result = await task_handler.process_task(task)
    assert result is not None
    