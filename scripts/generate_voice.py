import asyncio
import edge_tts
import os
from path_utils import OUTPUT_DIR

# Read generated script
script_path = f"{OUTPUT_DIR}/output_trial.txt"

with open(script_path, "r", encoding="utf-8") as f:
    text = f.read()

# Create output folder if missing
output_dir = OUTPUT_DIR

os.makedirs(output_dir, exist_ok=True)

# Output mp3 file
audio_file = os.path.join(output_dir, "narration.mp3")

# Voice options:
# en-US-GuyNeural
# en-US-AriaNeural
# en-US-DavisNeural
# en-US-JennyNeural

VOICE = "en-US-GuyNeural"

async def generate_voice():
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+5%"
    )
    await communicate.save(audio_file)
    print(f"Audio saved to: {audio_file}")

asyncio.run(generate_voice())