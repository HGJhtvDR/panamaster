"""
Утилиты для работы с базой данных (SQLAlchemy с SSL, reconnect).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
import time
from typing import Optional

class DatabaseManager:
    def __init__(self, connection_string: str, ssl_mode: bool = True):
        """
        Инициализация менеджера базы данных.
        
        Args:
            connection_string (str): Строка подключения к БД
            ssl_mode (bool): Использовать SSL для подключения
        """
        self.connection_string = connection_string
        self.ssl_mode = ssl_mode
        self.engine = None
        self.Session = None
        self.initialize()

    def initialize(self):
        """Инициализация подключения к базе данных."""
        try:
            # Настройка SSL для PostgreSQL
            if self.ssl_mode and 'postgresql' in self.connection_string:
                self.engine = create_engine(
                    self.connection_string,
                    connect_args={
                        'sslmode': 'require',
                        'client_encoding': 'utf8'
                    }
                )
            else:
                self.engine = create_engine(self.connection_string)

            self.Session = scoped_session(sessionmaker(bind=self.engine))
        except SQLAlchemyError as e:
            raise Exception(f"Ошибка инициализации БД: {str(e)}")

    def get_session(self):
        """Получение сессии БД с автоматическим переподключением."""
        try:
            return self.Session()
        except SQLAlchemyError:
            # Попытка переподключения
            time.sleep(1)
            self.initialize()
            return self.Session()

    def close_session(self, session):
        """Закрытие сессии БД."""
        if session:
            session.close() 