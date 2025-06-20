from datetime import timedelta
from typing import List, Optional

from .base import Config as BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    # Безопасность cookies
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    REMEMBER_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_DOMAIN: Optional[str] = None
    REMEMBER_COOKIE_DOMAIN: Optional[str] = None

    # База данных
    SQLALCHEMY_DATABASE_URI: str = "postgresql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Почта
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587
    MAIL_USE_TLS: bool = True
    MAIL_USERNAME: Optional[str] = "your-email@gmail.com"
    MAIL_PASSWORD: Optional[str] = "your-password"
    MAIL_DEFAULT_SENDER: Optional[str] = "your-email@gmail.com"

    # Логирование
    LOG_TO_STDOUT: bool = True
    LOG_LEVEL: str = "INFO"

    # Кэш
    CACHE_TYPE: str = "redis"
    CACHE_REDIS_URL: str = "redis://localhost:6379/1"
    CACHE_DEFAULT_TIMEOUT: int = 300

    # Сессии
    SESSION_TYPE: str = "redis"
    PERMANENT_SESSION_LIFETIME: timedelta = timedelta(minutes=30)

    # Пароли
    SECURITY_PASSWORD_SALT: str = "your-salt"
    SECURITY_PASSWORD_HASH: str = "bcrypt"
    SECURITY_PASSWORD_LENGTH_MIN: int = 8

    # CORS
    CORS_ORIGINS: List[str] = ["https://yourdomain.com"]
    CORS_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE"]
    CORS_ALLOW_HEADERS: List[str] = ["Content-Type", "Authorization"]
    CORS_EXPOSE_HEADERS: List[str] = []
    CORS_SUPPORTS_CREDENTIALS: bool = True
    CORS_MAX_AGE: int = 600

    # Загрузка файлов
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER: str = "uploads"

    # JWT
    JWT_SECRET_KEY: str = "your-jwt-secret"
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(days=30)

    # Лимиты
    RATELIMIT_DEFAULT: str = "200 per day"
    RATELIMIT_STORAGE_URL: str = "redis://localhost:6379/0"

    # API Rate Limiting
    API_RATE_LIMIT: str = "100 per hour"
    API_RATE_LIMIT_STORAGE_URL: str = "redis://localhost:6379/2"

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/3"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/4"
    CELERY_TASK_SERIALIZER: str = "json"
    CELERY_RESULT_SERIALIZER: str = "json"
    CELERY_ACCEPT_CONTENT: List[str] = ["json"]
    CELERY_TIMEZONE: str = "UTC"
    CELERY_ENABLE_UTC: bool = True
    CELERY_TASK_TRACK_STARTED: bool = True
    CELERY_TASK_TIME_LIMIT: int = 30 * 60  # 1800 секунд
    CELERY_TASK_SOFT_TIME_LIMIT: int = 25 * 60  # 1500 секунд
