"""
settings.py

Central configuration file for Orion.
"""

import os

from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# ================= Assistant =================

ASSISTANT_NAME = "Orion"

WAKE_WORD = "come back"

# ================= Speech =================

LANGUAGE = "en"

WHISPER_MODEL = "base"

SAMPLE_RATE = 16000

BLOCK_SIZE = 1024

# ================= API Keys =================

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")