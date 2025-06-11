"""
Конфигурация для тестового окружения.
"""

from .base import Config

class TestingConfig(Config):
    """
    Конфигурация для тестового окружения.
    Использует тестовую базу данных и отключает внешние сервисы.
    """
    
    # Включаем режим тестирования
    TESTING = True
    DEBUG = True
    
    # Используем SQLite для тестов
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
    # Отключаем CSRF для тестов
    WTF_CSRF_ENABLED = False
    
    # Отключаем внешние сервисы
    MAIL_SUPPRESS_SEND = True
    CACHE_TYPE = 'simple'
    
    # Настройки безопасности для тестов
    SECRET_KEY = 'test-secret-key'
    JWT_SECRET_KEY = 'test-jwt-secret'
    
    # Отключаем ограничения на загрузку файлов
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # Настройки для тестов
    PRESERVE_CONTEXT_ON_EXCEPTION = False
