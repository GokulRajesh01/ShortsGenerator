import os
import random
from moviepy.editor import (
    VideoFileClip,
    concatenate_videoclips,
    AudioFileClip
)
from moviepy.video.fx.all import crop
from path_utils import OUTPUT_DIR

# -----------------------------------
# PATHS
# -----------------------------------
clips_dir = "temp_assets"
audio_path = f"{OUTPUT_DIR}/narration.mp3"
output_path = f"{OUTPUT_DIR}/dynamic_background.mp4"

# -----------------------------------
# LOAD AUDIO
# -----------------------------------
audio = AudioFileClip(audio_path)
audio_duration = audio.duration
print(f"Audio duration: {audio_duration:.2f} sec")

# -----------------------------------
# LOAD CLIPS
# -----------------------------------
clip_files = [
    os.path.join(clips_dir, f)
    for f in os.listdir(clips_dir)
    if f.endswith(".mp4")
]
num_clips = len(clip_files)
print(f"Found {num_clips} clips")

# -----------------------------------
# SAFETY CHECK
# -----------------------------------
if num_clips == 0:
    raise Exception(
        "No clips found in temp_assets/"
    )

# -----------------------------------
# CALCULATE DURATION
# -----------------------------------
clip_duration = (
    audio_duration / num_clips
)
print(
    f"Each clip duration: "
    f"{clip_duration:.2f} sec"
)

# -----------------------------------
# CREATE SUBCLIPS
# -----------------------------------
final_clips = []
for clip_path in clip_files:
    print(f"\nProcessing: {clip_path}")
    clip = VideoFileClip(clip_path)

    # -----------------------------------
    # RANDOM START
    # -----------------------------------
    max_start = max(
        0,
        clip.duration - clip_duration
    )
    start_time = random.uniform(
        0,
        max_start
    )
    end_time = (
        start_time + clip_duration
    )
    print(f"Start: {start_time:.2f}")
    print(f"End: {end_time:.2f}")
    subclip = clip.subclip(
        start_time,
        end_time
    )

    # -----------------------------------
    # FORCE VERTICAL REELS FORMAT
    # -----------------------------------

    # ALWAYS resize by height
    # prevents thin slice artifacts
    subclip = subclip.resize(
        height=1920
    )

    # -----------------------------------
    # SAFETY CHECK AFTER RESIZE
    # -----------------------------------
    if subclip.w < 1080:
        scale_factor = (
            1080 / subclip.w
        )
        subclip = subclip.resize(
            scale_factor
        )

    # -----------------------------------
    # CENTER CROP
    # -----------------------------------
    subclip = crop(
        subclip,
        width=1080,
        height=1920,
        x_center=subclip.w / 2,
        y_center=subclip.h / 2
    )

    # -----------------------------------
    # FORCE CONSISTENT FPS
    # -----------------------------------
    subclip = subclip.set_fps(30)
    final_clips.append(subclip)

# -----------------------------------
# CONCATENATE
# -----------------------------------
final_video = concatenate_videoclips(
    final_clips,
    method="compose"
)

# -----------------------------------
# EXPORT
# -----------------------------------
final_video.write_videofile(
    output_path,
    fps=30,
    codec="libx264",
    bitrate="12000k",
    preset="slow",
    threads=4,
    audio=False
)
print(
    f"\nDynamic background created at:\n"
    f"{output_path}"
)