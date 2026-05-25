import subprocess
from path_utils import OUTPUT_DIR

video_input = f"{OUTPUT_DIR}/final_video.mp4"
subtitle_file = f"{OUTPUT_DIR}/subtitles.ass"
video_output = f"{OUTPUT_DIR}/final_video_subtitles.mp4"

subtitle_file_fixed = (
    subtitle_file
    .replace("\\", "/")
    .replace(":", "\\:")
)

command = [
    "ffmpeg",
    "-y",
    "-i", video_input,
    "-vf",
    f"ass='{subtitle_file_fixed}'",
    "-c:v", "libx264",
    "-preset", "slow",
    "-crf", "18",
    "-b:v", "12000k",
    "-c:a", "copy",
    video_output
]
subprocess.run(command)
print(
    f"\nFinal subtitled video created at:\n{video_output}"
)