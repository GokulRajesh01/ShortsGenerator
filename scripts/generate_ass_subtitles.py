from path_utils import OUTPUT_DIR

# -----------------------------------
# PATHS
# -----------------------------------
script_path = f"{OUTPUT_DIR}/output_trial.txt"
ass_path = f"{OUTPUT_DIR}/subtitles.ass"

# -----------------------------------
# READ SCRIPT
# -----------------------------------
with open(script_path, "r", encoding="utf-8") as f:
    text = f.read()

# -----------------------------------
# SPLIT INTO WORD GROUPS
# -----------------------------------
words = text.split()
chunks = []
chunk_size = 3
for i in range(0, len(words), chunk_size):
    chunk = " ".join(
        words[i:i + chunk_size]
    )
    chunks.append(
        chunk.upper()
    )

# -----------------------------------
# ASS HEADER
# -----------------------------------
header = """
[Script Info]
Title: TikTok Style Subtitles
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding

Style: Default,Arial,52,&H00FFFFFF,&H0000FFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,0,2,50,50,350,1

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
start_time = 0.0
for chunk in chunks:
    # Dynamic timing
    word_count = len(chunk.split())
    duration_per_chunk = max(
        0.65,
        word_count * 0.32
    )
    end_time = start_time + duration_per_chunk
    start_ass = format_ass_time(start_time)
    end_ass = format_ass_time(end_time)
    event = (
        f"Dialogue: 0,"
        f"{start_ass},"
        f"{end_ass},"
        f"Default,,0,0,0,,"
        f"{chunk}"
    )
    events.append(event)
    start_time = end_time

# -----------------------------------
# WRITE FILE
# -----------------------------------
with open(ass_path, "w", encoding="utf-8") as f:
    f.write(header)
    for event in events:
        f.write(event + "\n")
        
print(f"\nASS subtitles created at:\n{ass_path}")