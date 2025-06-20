from datetime import timedelta
from typing import List, Optional

from flask import Flask


class Config:
    DEBUG: bool = False
    TESTING: bool = False

    # Безопасность cookies
    SESSION_COOKIE_SECURE: bool = False
    REMEMBER_COOKIE_SECURE: bool = False
    SESSION_COOKIE_HTTPONLY: bool = True
    REMEMBER_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: Optional[str] = None
    REMEMBER_COOKIE_SAMESITE: Optional[str] = None
    SESSION_COOKIE_DOMAIN: Optional[str] = None
    REMEMBER_COOKIE_DOMAIN: Optional[str] = None

    # База данных
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Почта
    MAIL_SERVER: Optional[str] = None
    MAIL_PORT: Optional[int] = None
    MAIL_USE_TLS: Optional[bool] = None
    MAIL_USERNAME: Optional[str] = None
    MAIL_PASSWORD: Optional[str] = None
    MAIL_DEFAULT_SENDER: Optional[str] = None

    # Логирование
    LOG_TO_STDOUT: Optional[bool] = None
    LOG_LEVEL: Optional[str] = None

    # Кэш
    CACHE_TYPE: Optional[str] = None
    CACHE_REDIS_URL: Optional[str] = None
    CACHE_DEFAULT_TIMEOUT: Optional[int] = None

    # Сессии
    SESSION_TYPE: Optional[str] = None
    PERMANENT_SESSION_LIFETIME: timedelta = timedelta(minutes=20)

    # Пароли
    SECURITY_PASSWORD_SALT: Optional[str] = None
    SECURITY_PASSWORD_HASH: Optional[str] = None
    SECURITY_PASSWORD_LENGTH_MIN: int = 8

    # CORS
    CORS_ORIGINS: List[str] = []
    CORS_METHODS: List[str] = []
    CORS_ALLOW_HEADERS: List[str] = []
    CORS_EXPOSE_HEADERS: List[str] = []
    CORS_SUPPORTS_CREDENTIALS: bool = True
    CORS_MAX_AGE: int = 600

    # Загрузка файлов
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER: str = "uploads"

    # JWT
    JWT_SECRET_KEY: Optional[str] = None
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(days=30)

    # Лимиты
    RATELIMIT_DEFAULT: Optional[str] = None
    RATELIMIT_STORAGE_URL: Optional[str] = None

    # API Rate Limiting
    API_RATE_LIMIT: Optional[str] = None
    API_RATE_LIMIT_STORAGE_URL: Optional[str] = None

    # Celery
    CELERY_BROKER_URL: Optional[str] = None
    CELERY_RESULT_BACKEND: Optional[str] = None
    CELERY_TASK_SERIALIZER: Optional[str] = None
    CELERY_RESULT_SERIALIZER: Optional[str] = None
    CELERY_ACCEPT_CONTENT: List[str] = []
    CELERY_TIMEZONE: Optional[str] = None
    CELERY_ENABLE_UTC: Optional[bool] = None
    CELERY_TASK_TRACK_STARTED: Optional[bool] = None
    CELERY_TASK_TIME_LIMIT: Optional[int] = None
    CELERY_TASK_SOFT_TIME_LIMIT: Optional[int] = None

    @staticmethod
    def init_app(app: Flask) -> None:
        # Заглушка под кастомные инициализации — logging, мониторинг и т.п.
        pass
