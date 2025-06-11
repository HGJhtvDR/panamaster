"""
Конфигурации для разных окружений (development, production, testing).
"""

import os
from .base import Config
from .dev import DevelopmentConfig
from .prod import ProductionConfig
from .test import TestingConfig

# Словарь конфигураций для разных окружений
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """
    Получение конфигурации на основе переменной окружения FLASK_ENV.
    Если FLASK_ENV не установлен, используется конфигурация по умолчанию.
    """
    config_name = os.getenv('FLASK_ENV', 'default')
    return config[config_name] 