from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {"default": {"ENGINE": "django.db.backends.mysql", "OPTIONS": {}}}
