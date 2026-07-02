"""
settings.py

Central configuration file for Orion.

Responsibilities
----------------
- Store global configuration values.
- Load environment variables safely.
- Provide a single source of truth for constants.

This module does NOT:
- Contain business logic
- Handle speech or commands
"""

import os
from dotenv import load_dotenv

# ================= LOAD ENV =================

load_dotenv()

# ================= ASSISTANT =================

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Orion")

WAKE_WORD = os.getenv("WAKE_WORD", "come back")

# ================= SPEECH =================

LANGUAGE = os.getenv("LANGUAGE", "en-US")

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")

SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", 16000))

BLOCK_SIZE = int(os.getenv("BLOCK_SIZE", 1024))

# ================= SYSTEM =================

DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Pune")

# ================= API KEYS =================

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")

# ================= SAFETY CHECK =================

if not WEATHER_API_KEY:
    print("WARNING: WEATHER_API_KEY is missing in .env file")