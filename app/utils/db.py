"""
Утилиты для работы с базой данных (SQLAlchemy с SSL, reconnect).
"""

import time
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class DatabaseManager:
    def __init__(self, connection_string: str, ssl_mode: bool = True) -> None:
        """
        Инициализация менеджера базы данных.

        Args:
            connection_string (str): Строка подключения к БД
            ssl_mode (bool): Использовать SSL для подключения
        """
        self.connection_string = connection_string
        self.ssl_mode = ssl_mode
        self.engine = None
        self.Session: Optional[scoped_session] = None
        self.initialize()

    def initialize(self) -> None:
        """Инициализация подключения к базе данных."""
        try:
            if self.ssl_mode and "postgresql" in self.connection_string:
                self.engine = create_engine(
                    self.connection_string,
                    connect_args={"sslmode": "require", "client_encoding": "utf8"},
                )
            else:
                self.engine = create_engine(self.connection_string)

            self.Session = scoped_session(sessionmaker(bind=self.engine))
        except SQLAlchemyError as e:
            raise RuntimeError("Ошибка инициализации БД") from e

    def get_session(self) -> Session:
        """Получение сессии БД с автоматическим переподключением."""
        try:
            return self.Session()
        except SQLAlchemyError:
            time.sleep(1)
            self.initialize()
            return self.Session()

    def close_session(self, session: Optional[Session]) -> None:
        """Закрытие сессии БД."""
        if session:
            session.close()
