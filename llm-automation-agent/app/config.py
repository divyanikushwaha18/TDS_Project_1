import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
    DATA_DIR = "/data"
    API_URL = "https://api.aiproxy.xyz"  # Replace with actual API URL

settings = Settings()

