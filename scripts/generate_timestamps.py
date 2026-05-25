import whisper
import json

from path_utils import OUTPUT_DIR

# -----------------------------------
# PATHS
# -----------------------------------
audio_path = f"{OUTPUT_DIR}/narration.mp3"
output_path = f"{OUTPUT_DIR}/timestamps.json"

# -----------------------------------
# LOAD MODEL
# -----------------------------------
print("Loading Whisper model...")
model = whisper.load_model("base")

# tiny  -> fastest
# base  -> better quality

# -----------------------------------
# TRANSCRIBE
# -----------------------------------
print("Generating timestamps...")
result = model.transcribe(
    audio_path,
    word_timestamps=True
)

# -----------------------------------
# SAVE JSON
# -----------------------------------
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(
        result,
        f,
        indent=2
    )
print(f"\nTimestamps saved at:\n{output_path}")