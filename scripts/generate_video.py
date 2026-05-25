import subprocess
from path_utils import OUTPUT_DIR

background_video = f"{OUTPUT_DIR}/dynamic_background.mp4"
audio_file = f"{OUTPUT_DIR}/narration.mp3"
output_video = f"{OUTPUT_DIR}/final_video.mp4"

command = [
    "ffmpeg",
    "-y",
    "-i", background_video,
    "-i", audio_file,
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    output_video
]
subprocess.run(command)
print(f"Final video created at: {output_video}")