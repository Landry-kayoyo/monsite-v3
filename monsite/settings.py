"""
Django settings for monsite project.
Déployé sur PythonAnywhere
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Sécurité
# ----------------------------
SECRET_KEY = 'django-insecure-kj@98bm#s#mh29677&s=5_%ni06%t_hh$+w1_yit16$1uma=)7'

# ⚠️ En production, toujours mettre DEBUG=False
DEBUG = False

# Nom de domaine PythonAnywhere
ALLOWED_HOSTS = ['Landrykayoyo.pythonanywhere.com']

# ----------------------------
# Applications
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # ton app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # dossier templates global si tu en as un
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'monsite-v3.wsgi.application'

# ----------------------------
# Base de données
# (sur PythonAnywhere gratuit → utilise SQLite, pas PostgreSQL)
# ----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# ----------------------------
# Validation des mots de passe
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------------
# Internationalisation
# ----------------------------
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Kinshasa'
USE_I18N = True
USE_TZ = True

# ----------------------------
# Fichiers statiques et médias
# ----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # dossier static de ton projet
STATIC_ROOT = BASE_DIR / "staticfiles"    # collectstatic ira ici

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------------
# Email (avec Gmail)
# ----------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kayoyolandry@gmail.com'
EMAIL_HOST_PASSWORD = 'vddv nyws uuzx lhud'  # mot de passe d'application
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_EMAIL = 'kayoyolandry@gmail.com'  # ton email de réception

# ----------------------------
# Clé par défaut
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
