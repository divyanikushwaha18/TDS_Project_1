import httpx
from ..config import settings

class LLMService:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    async def classify_task(self, task_description: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.API_URL}/v1/chat/completions",
                headers=self.headers,
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": "Classify the task type."},
                        {"role": "user", "content": task_description}
                    ]
                }
            )
            return response.json()["choices"][0]["message"]["content"]
        