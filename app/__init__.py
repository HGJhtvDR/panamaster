import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Optional

from flask import Flask, request
from flask_babel import Babel
from flask_caching import Cache
from flask_compress import Compress
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_principal import Permission, Principal, RoleNeed
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.errors import init_error_handlers

# from app.models.user import User  # ❌ Комментарий — файл отсутствует
from app.security import apply_security_headers
from config import config

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация расширений
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
babel = Babel()
cache = Cache()
limiter = Limiter(key_func=get_remote_address)
compress = Compress()
principal = Principal()
csrf = CSRFProtect()

# Определение ролей и разрешений
admin_role = RoleNeed("admin")
user_role = RoleNeed("user")
admin_permission = Permission(admin_role)
user_permission = Permission(user_role)


# Заглушка для user_loader — вернётся None, чтобы не падал Flask-Login
@login_manager.user_loader
def load_user(user_id: int) -> Optional[object]:
    return None
    # try:
    #     return User.query.get(int(user_id))
    # except Exception:
    #     return None


def create_app(config_name: str) -> Flask:
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )
    # Минимальная конфигурация
    app.config["SECRET_KEY"] = "dev"
    # Регистрируем только public blueprint
    from app.routes.public import bp as public_blueprint

    app.register_blueprint(public_blueprint)
    return app
