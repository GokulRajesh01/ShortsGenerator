import requests
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

print(API_KEY)
response = requests.get(url)

print(response.status_code)
print(response.text)