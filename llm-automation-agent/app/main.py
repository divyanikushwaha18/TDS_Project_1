from fastapi import FastAPI, HTTPException
from app.services.task_handler import TaskHandler
from .config import settings

app = FastAPI()
task_handler = TaskHandler(settings.AIPROXY_TOKEN)

@app.post("/run")
async def run_task(task: str):
    try:
        result = await task_handler.process_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    try:
        if not path.startswith(settings.DATA_DIR):
            raise HTTPException(status_code=400, detail="Invalid path")
        return await task_handler.read_file(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

