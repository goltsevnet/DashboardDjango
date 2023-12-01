import os, sys

sys.path.insert(0, "/var/www/u1768503/data/www/dashboard.goltsev.ru/app")
sys.path.insert(1, "/var/www/u1768503/data/dashboard_venv/lib/python3.10/site-packages")
os.environ["DJANGO_SETTINGS_MODULE"] = "app.config.settings.production"
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
