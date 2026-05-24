# AI Short Videos Factory

An experimental AI-powered short-form video generation pipeline.
---

# Features Implemented

- Gemini API integration
- AI narration script generation
- Edge-TTS voice generation
- Automated MP3 narration creation
- Automated MP4 video generation
- Modular Python script structure

---

# Current Pipeline

Topic
↓
Gemini API
↓
Narration Script
↓
Edge-TTS
↓
Narration MP3
↓
FFmpeg
↓
Final MP4

---

# Project Structure

```text
ai-shortvideos-factory/
│
├── scripts/
│   ├── generate_script.py
│   ├── generate_video.py
│   ├── generate_voice.py
│   ├── list_models.py
│   └── path_utils.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Tech Stack

| Purpose | Tool |
|---|---|
| Script Generation | Gemini API |
| Voice Generation | Edge-TTS |
| Video Rendering | FFmpeg |
| Language | Python |

---

# Setup

## Create Virtual Environment

### Windows

```bash
python -m venv generator_environment
generator_environment\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install FFmpeg

Download:
https://ffmpeg.org/download.html

Verify installation:

```bash
ffmpeg -version
```

---

## Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running Scripts

## Generate AI Script

```bash
python scripts/generate_script.py
```

---

## Generate Narration Voice

```bash
python scripts/generate_voice.py
```

---

## Generate Final Video

```bash
python scripts/generate_video.py
```

---

# Current Status

Project is currently in:
- MVP stage
- local execution only
- experimental automation phase

Future plans include:
- subtitles
- automated clip switching
- Telegram approval workflow
- automated uploads
- orchestration with n8n

---

# Disclaimer

This project is experimental and intended for learning and automation practice.