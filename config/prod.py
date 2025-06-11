"""
Конфигурация для продакшен-окружения.
"""

from .base import Config

class ProductionConfig(Config):
    """
    Конфигурация для продакшен-окружения.
    Включает настройки безопасности, оптимизации и мониторинга.
    """
    
    # Отключаем режим отладки
    DEBUG = False
    TESTING = False
    
    # Настройки безопасности
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    
    # Настройки базы данных
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/panamaster'
    
    # Настройки почты
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your-email@gmail.com'
    MAIL_PASSWORD = 'your-app-password'
    
    # Настройки логирования
    LOG_TO_STDOUT = True
    LOG_LEVEL = 'INFO'
    
    # Настройки кэширования
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = 'redis://redis:6379/0'
    
    # Настройки сессий
    SESSION_TYPE = 'redis'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 час
    
    # Настройки безопасности
    SECURITY_PASSWORD_SALT = 'your-salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_LENGTH_MIN = 8
    
    # Настройки CORS
    CORS_ORIGINS = ['https://yourdomain.com']
    
    # Настройки загрузки файлов
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = '/app/uploads'
    
    # Настройки JWT
    JWT_SECRET_KEY = 'your-jwt-secret'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 час
    JWT_REFRESH_TOKEN_EXPIRES = 2592000  # 30 дней 