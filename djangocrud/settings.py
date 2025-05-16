from pathlib import Path
import os
import dj_database_url 
# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

DEBUG = 'RENDER' not in os.environ
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Redirección después de login
LOGIN_REDIRECT_URL = 'sesiones'

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# Autenticación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Configuración actualizada de allauth
ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_UNIQUE_EMAIL = True

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]

# URLs
ROOT_URLCONF = 'djangocrud.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'djangocrud.wsgi.application'

# Base de datos
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # para desarrollo
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    # para producción

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración del sitio (requerido por allauth)
SITE_ID = 1

