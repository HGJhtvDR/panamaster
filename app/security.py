import base64
import hashlib
import hmac
import secrets
from functools import wraps
from typing import Any, Callable

from flask import Response, request
from flask_login import UserMixin
from werkzeug.security import check_password_hash


def generate_csrf_token() -> str:
    """Генерирует безопасный CSRF токен"""
    return secrets.token_hex(32)


def hash_password(password: str) -> str:
    """Безопасное хеширование пароля с использованием PBKDF2"""
    salt = secrets.token_hex(16)
    iterations = 100_000
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations)
    return f"{salt}${iterations}${base64.b64encode(key).decode('utf-8')}"


def verify_password(password: str, hashed: str) -> bool:
    """Проверка пароля"""
    salt, iterations, stored_key = hashed.split("$")
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), int(iterations))
    return hmac.compare_digest(base64.b64encode(key).decode("utf-8"), stored_key)


def apply_security_headers(response: Response) -> Response:
    """Применяет заголовки безопасности к ответу"""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
        "img-src 'self' data:; font-src 'self' https://cdnjs.cloudflare.com;"
    )
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

    if request.endpoint == "auth.logout":
        response.headers["Clear-Site-Data"] = '"cache", "cookies", "storage"'

    return response


def security_headers(f: Callable[..., Response]) -> Callable[..., Response]:
    """Декоратор для применения заголовков безопасности к маршруту"""

    @wraps(f)
    def decorated_function(*args: Any, **kwargs: Any) -> Response:
        response = f(*args, **kwargs)
        return apply_security_headers(response)

    return decorated_function


class User(UserMixin):
    """User model for authentication."""

    def __init__(self, username: str, password_hash: str) -> None:
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)

    def get_id(self) -> str:
        """Get the user ID."""
        return self.username
