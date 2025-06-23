from flask import Blueprint

bp = Blueprint("public", __name__)


@bp.route("/")
def index():
    return "<h1>Тестовая главная страница тест 2</h1><p>Пример простого содержимого.</p>"


__all__ = ["bp"]
