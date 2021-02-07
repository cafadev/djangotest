from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']
SECRET_KEY = '@yce&^=ue^lqa_w)wa1mc$d_y8qm74gdqwh+es_(^awggc0$+b'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}