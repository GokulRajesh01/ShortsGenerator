import requests
import os
import time
from dotenv import load_dotenv
from path_utils import OUTPUT_DIR

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MAX_RETRIES = 3

prompt = """
Write ONLY a narration script for a viral 35-second YouTube Short about AI replacing software engineers.

Rules:
- Plain narration text only
- No markdown
- No bullet points
- No scene directions
- No titles
- No labels
- No formatting
- Maximum 90 words
- Short punchy sentences
- Dramatic hook
"""

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

for attempt in range(MAX_RETRIES):
    response = requests.post(url, json=payload, headers={
        "Content-Type" : "application/json"
    })
    if response.status_code == 200:
        break
    elif response.status_code == 429:
        print("Rate limited. Waiting...")
        time.sleep(15)
    else:
        print(response.text)
        break

print(response.status_code)
print(response.text)
    
data = response.json()

if response.status_code != 200:
    print("API ERROR")
    print(data)
    exit()

script = data["candidates"][0]["content"]["parts"][0]["text"]

print(script)

with open(f"{OUTPUT_DIR}/output_trial.txt", "w", encoding="utf-8") as f:
    f.write(script)