# AI Short Videos Factory

An automated AI-powered short-form content generation pipeline for:
- YouTube Shorts
- Instagram Reels
- TikTok

This project generates:
- AI-written scripts
- AI voice narration
- Dynamic background videos
- Stylized subtitles
- Final rendered short-form videos

---

# Current Pipeline

Topic Input
↓
Gemini Script Generation
↓
Edge-TTS Narration
↓
Dynamic Background Generation
↓
Video + Audio Merge
↓
ASS Subtitle Generation
↓
FFmpeg Subtitle Burn
↓
Final Short-form Video

---

# Features

## AI Script Generation
Uses Google Gemini API to generate:
- Hook-driven scripts
- Short-form optimized narration
- Retention-oriented pacing

---

## Free AI Voice Generation
Uses:
- edge-tts

No ElevenLabs subscription required.

---

## Dynamic Video Backgrounds
Randomly:
- selects clips
- trims segments
- stitches dynamic vertical videos

This avoids:
- static slideshow feel
- repetitive visuals

---

## TikTok/Shorts Style Subtitles
Uses:
- ASS subtitles
- FFmpeg burn-in

Supports:
- large captions
- chunk-based subtitles
- retention-focused placement

---

# Tech Stack

## AI
- Gemini API

## TTS
- edge-tts

## Video Processing
- MoviePy
- FFmpeg

## Subtitle Engine
- ASS subtitles
- FFmpeg rendering

## Language
- Python

---

# Folder Structure

ai-shortvideos-factory/
│
├── assets/
│   └── background clips
│
├── output/
│   ├── narration.mp3
│   ├── dynamic_background.mp4
│   ├── final_video.mp4
│   ├── subtitles.ass
│   └── final_video_subtitles.mp4
│
├── scripts/
│   ├── generate_script.py
│   ├── generate_voice.py
│   ├── create_dynamic_background.py
│   ├── merge_audio_video.py
│   ├── generate_ass_subtitles.py
│   └── burn_ass_subtitles.py
│
├── .env
├── requirements.txt
└── README.md

---

# Setup

## 1. Clone Repo

```bash
git clone <repo-url>
cd ai-shortvideos-factory
```

---

## 2. Create Virtual Environment

```bash
python -m venv generator_environment
```

### Activate venv (Windows)

```bash
generator_environment\Scripts\activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in project root:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# FFmpeg Setup

Install FFmpeg and ensure this works:

```bash
ffmpeg -version
```

---

# Current Workflow

## 1. Generate Script

```bash
python scripts/generate_script.py
```

---

## 2. Generate Voice

```bash
python scripts/generate_voice.py
```

---

## 3. Generate Dynamic Background

```bash
python scripts/create_dynamic_background.py
```

---

## 4. Merge Video + Audio

```bash
python scripts/merge_audio_video.py
```

---

## 5. Generate ASS Subtitles

```bash
python scripts/generate_ass_subtitles.py
```

---

## 6. Burn ASS Subtitles

```bash
python scripts/burn_ass_subtitles.py
```