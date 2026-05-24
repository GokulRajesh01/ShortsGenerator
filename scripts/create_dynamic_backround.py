import os
import random

from moviepy.editor import (
    VideoFileClip,
    concatenate_videoclips,
    AudioFileClip
)
from moviepy.video.fx.all import crop
from path_utils import ASSETS_DIR, OUTPUT_DIR

# -----------------------------------
# PATHS
# -----------------------------------

clips_dir = ASSETS_DIR
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
# CALCULATE DURATION PER CLIP
# -----------------------------------

clip_duration = audio_duration / num_clips

print(f"Each clip duration: {clip_duration:.2f} sec")

# -----------------------------------
# CREATE RANDOM SUBCLIPS
# -----------------------------------

final_clips = []

for clip_path in clip_files:

    clip = VideoFileClip(clip_path)

    max_start = max(
        0,
        clip.duration - clip_duration
    )

    start_time = random.uniform(
        0,
        max_start
    )

    end_time = start_time + clip_duration

    print(f"\nClip: {clip_path}")
    print(f"Start: {start_time:.2f}")
    print(f"End: {end_time:.2f}")

    subclip = clip.subclip(
        start_time,
        end_time
    )

    # Resize to vertical
    subclip = subclip.resize(
        height=1920
    )

    # Center crop
    subclip = crop(
        subclip,
        x_center=subclip.w / 2,
        width=1080,
        height=1920
    )

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
    audio=False
)

print(f"\nDynamic background created at:\n{output_path}")