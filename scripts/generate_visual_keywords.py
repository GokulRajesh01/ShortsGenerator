import json
import requests
import os
from dotenv import load_dotenv
from path_utils import OUTPUT_DIR
load_dotenv()

# -----------------------------------
# LOAD SCRIPT
# -----------------------------------
script_path = f"{OUTPUT_DIR}/output_trial.txt"
with open(script_path, "r", encoding="utf-8") as f:
    script = f.read()

# -----------------------------------
# GEMINI API
# -----------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

prompt = f"""
You are generating search keywords for highly engaging
short-form video footage for TikTok, Reels, and YouTube Shorts.

The visuals MUST feel:
- cinematic
- futuristic
- fast-paced
- high-tech
- visually stimulating
- cyberpunk
- neon
- dramatic
- modern
- intense

IMPORTANT:
Generate search terms that produce:
- glowing visuals
- moving technology shots
- animated screens
- futuristic city footage
- hackers
- AI robots
- server rooms
- cinematic coding scenes
- digital interfaces
- sci-fi technology aesthetics

AVOID:
- boring office footage
- static meetings
- generic business people
- bland corporate visuals
- slow visuals

GOOD EXAMPLES:
- futuristic technology
- cyberpunk city
- hacker computer
- AI robot
- glowing server room
- cinematic coding
- neon technology
- sci fi interface
- digital data flow
- futuristic UI
- hologram screen
- artificial intelligence animation
- tech tunnel
- abstract technology background

The visuals should feel like:
Netflix tech documentary + TikTok editing.

Return ONLY a JSON array.

Script:
{script}
"""

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}
response = requests.post(
    url,
    json=payload
)
data = response.json()

text = data["candidates"][0]["content"]["parts"][0]["text"]
print(text)

cleaned = (
    text
    .replace("```json", "")
    .replace("```", "")
    .strip()
)
keywords = json.loads(cleaned)
output_path = f"{OUTPUT_DIR}/visual_keywords.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(
        keywords,
        f,
        indent=2
    )
print(f"\nKeywords saved at:\n{output_path}")