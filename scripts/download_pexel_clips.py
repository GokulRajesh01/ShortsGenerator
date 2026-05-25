import os
import json
import requests
from dotenv import load_dotenv
from path_utils import OUTPUT_DIR
load_dotenv()

# -----------------------------------
# CONFIG
# -----------------------------------
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
HEADERS = {
    "Authorization": PEXELS_API_KEY
}
TEMP_DIR = "temp_assets"
os.makedirs(TEMP_DIR, exist_ok=True)

# -----------------------------------
# LOAD KEYWORDS
# -----------------------------------
keywords_path = f"{OUTPUT_DIR}/visual_keywords.json"
with open(keywords_path, "r", encoding="utf-8") as f:
    keywords = json.load(f)

# -----------------------------------
# DOWNLOAD FUNCTION
# -----------------------------------
def download_video(url, filename):
    response = requests.get(
        url,
        stream=True
    )
    with open(filename, "wb") as f:
        for chunk in response.iter_content(
            chunk_size=1024
        ):
            if chunk:
                f.write(chunk)

# -----------------------------------
# SEARCH + DOWNLOAD
# -----------------------------------
for i, keyword in enumerate(keywords):
    print(f"\nSearching: {keyword}")
    search_url = (
        f"https://api.pexels.com/videos/search"
        f"?query={keyword}&per_page=3"
    )
    response = requests.get(
        search_url,
        headers=HEADERS
    )
    data = response.json()
    videos = data.get("videos", [])
    if not videos:
        print("No videos found.")
        continue
    selected_video = None

    # Prefer vertical videos first
    for video in videos:
        width = video.get("width", 0)
        height = video.get("height", 0)
        if height > width:
            selected_video = video
            break

    # fallback
    if selected_video is None:
        selected_video = videos[0]
    video_files = selected_video["video_files"]
    if not video_files:
        print("No downloadable files.")
        continue

    # Pick highest quality file
    best_file = max(
        video_files,
        key=lambda x: x.get("width", 0)
    )
    video_url = best_file["link"]
    output_file = (
        f"{TEMP_DIR}/clip_{i}.mp4"
    )
    print(f"Downloading to: {output_file}")
    download_video(
        video_url,
        output_file
    )
print("\nDone downloading clips.")