import os
from datetime import timedelta

from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-string'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    
    # Redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # Celery
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'
    
    # CORS
    CORS_ORIGINS = ['http://localhost:5000', 'https://yourdomain.com']
    
    # File upload
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads')
    
    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # Rate limiting
    RATELIMIT_DEFAULT = "200 per day;50 per hour;10 per minute"
    RATELIMIT_STORAGE_URL = "memory://"
    
    # Logging
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

    # Настройки WTF
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = SECRET_KEY
    WTF_CSRF_TIME_LIMIT = 3600  # 1 час

    # Настройки кэширования
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = REDIS_URL
    CACHE_DEFAULT_TIMEOUT = 300

    # Настройки сжатия
    COMPRESS_MIMETYPES = [
        "text/html",
        "text/css",
        "text/xml",
        "application/json",
        "application/javascript",
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500

    # Настройки безопасности
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_LENGTH_MIN = 8
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": True}

    # Telegram
    TELEGRAM_TOKEN = SECRET_KEY

    # API
    API_KEY = SECRET_KEY

    # Настройки локализации
    LANGUAGES = ["ru", "en"]
    BABEL_DEFAULT_LOCALE = "ru"

    # Настройки API
    API_RATE_LIMIT = "100 per minute"

    # Security Headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_CONTENT_TYPE_OPTIONS = 'nosniff'
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    X_XSS_PROTECTION = '1; mode=block'
    
    # Content Security Policy
    CONTENT_SECURITY_POLICY = {
        'default-src': "'self'",
        'script-src': "'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net",
        'style-src': "'self' 'unsafe-inline' https://cdn.jsdelivr.net",
        'img-src': "'self' data: https:",
        'font-src': "'self' https://cdn.jsdelivr.net",
        'connect-src': "'self'",
        'frame-ancestors': "'none'",
        'form-action': "'self'",
        'base-uri': "'self'",
        'object-src': "'none'",
        'frame-src': "'none'",
        'media-src': "'none'",
        'worker-src': "'none'",
        'manifest-src': "'self'",
        'prefetch-src': "'self'",
        'upgrade-insecure-requests': '',
        'block-all-mixed-content': ''
    }
    
    # CORS settings
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization', 'X-Requested-With']
    CORS_EXPOSE_HEADERS = ['Content-Range', 'X-Content-Range']
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_MAX_AGE = 3600

    # Password Policy
    PASSWORD_MIN_LENGTH = 12
    PASSWORD_REQUIRE_UPPER = True
    PASSWORD_REQUIRE_LOWER = True
    PASSWORD_REQUIRE_DIGITS = True
    PASSWORD_REQUIRE_SPECIAL = True
    
    # Session Security
    SESSION_COOKIE_NAME = '__Host-session'
    REMEMBER_COOKIE_NAME = '__Host-remember'
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SAMESITE = 'Lax'
    
    # File Upload Security
    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx']
    UPLOAD_PATH = 'uploads'

    @staticmethod
    def init_app(app):
        pass
