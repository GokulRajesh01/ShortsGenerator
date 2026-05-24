import subprocess
import os
from path_utils import ASSETS_DIR, OUTPUT_DIR

background_video = f"{ASSETS_DIR}/background-video.mp4"
audio_file = f"{OUTPUT_DIR}/narration.mp3"
output_video = f"{OUTPUT_DIR}/final_video.mp4"

command = [
    "ffmpeg",
    "-y",
    "-i", background_video,
    "-i", audio_file,
    "-c:v", "copy",
    "-c:a", "aac",
    "-shortest",
    output_video
]

subprocess.run(command)
print(f"Final video created at: {output_video}")