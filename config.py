"""VELOCITY UKRAINIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY UKRAINIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "UKRAINIAN"
HANDLE = "@velocityukrainian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "uk",
    "name": "Ukrainian",
    "native_name": "Українська",
    "history_key": "ukrainian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "uk-UA-OstapNeural",
    "native_fallback_voice": "uk-UA-PolinaNeural",
    "native_engine": "edge",
    "native_lang_code": "uk",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "УКРАЇНСЬКА",
    "translit_label": "SAY IT LIKE",
    "greeting": "Привіт!",
    "encouragement": "Чудово!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "Мотивація", "rocket", "#A560E8"),
    ("Love", "Любов", "heart", "#FF4B4B"),
    ("Success", "Успіх", "trophy", "#F5A700"),
    ("Wisdom", "Мудрість", "book", "#A560E8"),
    ("Happiness", "Щастя", "smile", "#F5A700"),
    ("Self Improvement", "Саморозвиток", "leaf", "#58CC02"),
    ("Gratitude", "Вдячність", "heart", "#FF7A00"),
    ("Friendship", "Дружба", "users", "#00A889"),
    ("Hope", "Надія", "sun", "#FF7A00"),
    ("Creativity", "Креативність", "palette", "#E056A0"),
    ("Inner Peace", "Внутрішній Спокій", "lotus", "#00A889"),
    ("Confidence", "Впевненість", "shield", "#1CB0F6"),
    ("Perseverance", "Наполегливість", "mountain", "#FF7A00"),
    ("Inspiration", "Натхнення", "sparkles", "#A560E8"),
    ("Positive Life", "Позитивне Життя", "sun", "#58CC02"),
    ("Courage", "Хоробрість", "shield", "#FF4B4B"),
    ("Kindness", "Доброта", "heart", "#E056A0"),
    ("Patience", "Терпіння", "hourglass", "#00A889"),
    ("Forgiveness", "Прощення", "hands", "#FF7A00"),
    ("Strength", "Сила", "dumbbell", "#FF4B4B"),
    ("Joy", "Радість", "smile", "#F5A700"),
    ("Balance", "Баланс", "scale", "#00A889"),
    ("Growth", "Зростання", "sprout", "#58CC02"),
    ("Purpose", "Мета", "target", "#A560E8"),
    ("Mindfulness", "Усвідомленість", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnukrainian",
    "#ukrainianlessons",
    "#ukrainianforbeginners",
    "#languagelearning",
    "#ukrainianvocabulary",
    "#velocityukrainian",
    "#dailyukrainian",
    "#ukrainian",
    "#learnlanguages",
    "#speakukrainian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
