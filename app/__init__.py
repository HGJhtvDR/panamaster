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
from app.models.user import User
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


@login_manager.user_loader
def load_user(user_id: int) -> Optional[User]:
    try:
        return User.query.get(int(user_id))
    except Exception:
        return None


def create_app(config_name: str) -> Flask:
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Только для PostgreSQL
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgresql"):
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"connect_args": {"client_encoding": "utf8"}}

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    csrf.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    compress.init_app(app)
    principal.init_app(app)

    # CORS
    CORS(
        app,
        resources={
            r"/*": {
                "origins": app.config["CORS_ORIGINS"],
                "methods": app.config["CORS_METHODS"],
                "allow_headers": app.config["CORS_ALLOW_HEADERS"],
                "expose_headers": app.config["CORS_EXPOSE_HEADERS"],
                "supports_credentials": app.config["CORS_SUPPORTS_CREDENTIALS"],
                "max_age": app.config["CORS_MAX_AGE"],
            }
        },
    )

    # Настройка логирования
    if not app.debug and not app.testing:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler("logs/panamaster.log", maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info("Panamaster startup")

    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Пожалуйста, войдите для доступа к этой странице."
    login_manager.login_message_category = "info"

    # Регистрация blueprints
    from app.routes.admin import admin as admin_blueprint
    from app.routes.api import api as api_blueprint
    from app.routes.articles import bp as articles_blueprint
    from app.routes.auth import auth as auth_blueprint
    from app.routes.company import bp as company_blueprint
    from app.routes.contact import bp as contact_blueprint
    from app.routes.jobs import bp as jobs_blueprint
    from app.routes.public import bp as public_blueprint
    from app.routes.services import bp as services_blueprint
    from app.routes.training import training as training_blueprint

    app.register_blueprint(public_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    app.register_blueprint(services_blueprint)
    app.register_blueprint(articles_blueprint)
    app.register_blueprint(training_blueprint)
    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(company_blueprint)
    app.register_blueprint(contact_blueprint)

    # Обработчики ошибок
    init_error_handlers(app)

    # Заголовки безопасности
    @app.after_request
    def add_security_headers(response):
        return apply_security_headers(response)

    # Контекст для шаблонов
    @app.context_processor
    def inject_now():
        return {"now": datetime.utcnow(), "request": request}

    # Создание таблиц базы данных
    with app.app_context():
        try:
            db.create_all()
            logger.info("База данных успешно инициализирована")
        except Exception as e:
            logger.error(f"Ошибка при инициализации базы данных: {str(e)}")

    return app
