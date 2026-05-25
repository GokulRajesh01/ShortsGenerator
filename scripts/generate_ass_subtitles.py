import json
from path_utils import OUTPUT_DIR

# -----------------------------------
# PATHS
# -----------------------------------
json_path = f"{OUTPUT_DIR}/timestamps.json"
ass_path = f"{OUTPUT_DIR}/subtitles.ass"

# -----------------------------------
# LOAD TIMESTAMPS
# -----------------------------------
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# -----------------------------------
# COLLECT WORDS
# -----------------------------------
all_words = []
for segment in data["segments"]:
    for word in segment["words"]:
        all_words.append(word)

# -----------------------------------
# SETTINGS
# -----------------------------------
chunk_size = 2
SYNC_OFFSET = 0.22

# -----------------------------------
# GROUP WORDS
# -----------------------------------
chunks = []
for i in range(0, len(all_words), chunk_size):
    word_group = all_words[i:i + chunk_size]
    if not word_group:
        continue
    text = " ".join(
        w["word"].strip()
        for w in word_group
    ).upper()
    # Delay subtitles slightly
    start = max(
        0,
        word_group[0]["start"] + SYNC_OFFSET
    )
    end = (
        word_group[-1]["end"] + SYNC_OFFSET
    )
    chunks.append({
        "text": text,
        "start": start,
        "end": end
    })

# -----------------------------------
# ASS HEADER
# -----------------------------------
header = """
[Script Info]
Title: Whisper Synced Subtitles
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding

Style: Default,Arial,56,&H00FFFFFF,&H0000FFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,0,2,50,50,320,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# -----------------------------------
# TIME FORMATTER
# -----------------------------------
def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours}:{minutes:02}:{secs:05.2f}"

# -----------------------------------
# CREATE EVENTS
# -----------------------------------
events = []
for chunk in chunks:
    start_ass = format_ass_time(
        chunk["start"]
    )
    end_ass = format_ass_time(
        chunk["end"]
    )
    event = (
        f"Dialogue: 0,"
        f"{start_ass},"
        f"{end_ass},"
        f"Default,,0,0,0,,"
        f"{chunk['text']}"
    )
    events.append(event)

# -----------------------------------
# WRITE FILE
# -----------------------------------
with open(ass_path, "w", encoding="utf-8") as f:
    f.write(header)
    for event in events:
        f.write(event + "\n")
print(
    f"\nWhisper-synced ASS subtitles created at:\n{ass_path}"
)