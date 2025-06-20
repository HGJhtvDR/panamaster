"""
Конфигурации для разных окружений (development, production, testing).
"""

import os
from typing import Dict, Type

from config.base import Config
from config.dev import DevelopmentConfig
from config.prod import ProductionConfig
from config.test import TestingConfig

# Словарь конфигураций для разных окружений
config_by_name: Dict[str, Type[Config]] = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}


# Глобально доступная точка входа для получения конфигурации по имени
def get_config(name: str = None) -> Type[Config]:
    """
    Получение конфигурации на основе переменной окружения FLASK_ENV
    или явного параметра `name`. Если не задано — используется "development".
    """
    env = name or os.getenv("FLASK_ENV", "development")
    return config_by_name.get(env, DevelopmentConfig)


# Экспорт конфигураций по имени, чтобы обращаться как config["production"]
config: Dict[str, Type[Config]] = config_by_name
