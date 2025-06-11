import pytest

from app import create_app, db
from app.models.user import User
# from config.test import TestingConfig  # больше не нужен импорт класса


@pytest.fixture
def app():
    """Создает и возвращает тестовое приложение Flask"""
    app = create_app('testing')
    return app


@pytest.fixture
def client(app):
    """Создает тестовый клиент"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Создает тестовый CLI runner"""
    return app.test_cli_runner()


@pytest.fixture
def app_context(app):
    with app.app_context():
        yield


@pytest.fixture
def db_session(app_context):
    db.create_all()
    yield db.session
    db.session.remove()
    db.drop_all()


@pytest.fixture
def test_user(app):
    """Создает тестового пользователя"""
    user = User(username="testuser", email="test@example.com", password="testpassword")
    db.session.add(user)
    db.session.commit()
    return user
