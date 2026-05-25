from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Common folders
ASSETS_DIR = ROOT_DIR / "temp_assets"
OUTPUT_DIR = ROOT_DIR / "output"
SCRIPTS_DIR = ROOT_DIR / "scripts"

# Ensure output folder exists
OUTPUT_DIR.mkdir(exist_ok=True)