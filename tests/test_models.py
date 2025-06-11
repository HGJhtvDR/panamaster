import pytest
from werkzeug.security import check_password_hash

from app.models.user import User


def test_user_creation(app):
    """Тест создания пользователя"""
    user = User(username="testuser", email="test@example.com")
    user.set_password("testpassword")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.check_password("testpassword")


def test_user_repr(app):
    """Тест строкового представления пользователя"""
    user = User(username="testuser", email="test@example.com")
    assert str(user) == "<User testuser>"


def test_user_password(app):
    """Тест хеширования пароля"""
    user = User(username="testuser", email="test@example.com")
    user.set_password("testpassword")
    assert user.check_password("testpassword")
    assert not user.check_password("wrongpassword")
