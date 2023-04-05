from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

"""
Для продукции следует использовать Postgres или MySQL
https://docs.djangoproject.com/en/4.1/ref/databases/
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
