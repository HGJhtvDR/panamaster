from typing import Callable, cast

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask_principal import Permission, RoleNeed
from werkzeug.wrappers import Response

from app import db
from app.models.article import Article
from app.models.category import Category
from app.models.course import Course
from app.models.job import Job
from app.models.knowledge import Knowledge
from app.models.log import Log
from app.models.portfolio import Portfolio
from app.models.product import Product
from app.models.project import Project
from app.models.service import Service
from app.models.user import User

from . import admin

admin_permission = Permission(RoleNeed("admin"))


@admin.before_request
@login_required
@admin_permission.require()
def before_request() -> None:
    pass


def admin_required(f: Callable) -> Callable:
    def decorated_function(*args: object, **kwargs: object) -> object:
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("У вас нет доступа к этой странице", "error")
            return redirect(url_for("public.index"))
        return f(*args, **kwargs)

    decorated_function.__name__ = f.__name__
    return decorated_function


@admin.route("/")
@login_required
@admin_required
def index() -> Response:
    return cast(Response, render_template("admin/index.html"))


@admin.route("/dashboard")
def dashboard() -> Response:
    stats = {
        "users": User.query.count(),
        "services": Service.query.count(),
        "articles": Article.query.count(),
        "courses": Course.query.count(),
        "jobs": Job.query.count(),
        "projects": Project.query.count(),
        "categories": Category.query.count(),
        "products": Product.query.count(),
        "portfolios": Portfolio.query.count(),
        "knowledge": Knowledge.query.count(),
    }
    return cast(Response, render_template("admin/dashboard.html", stats=stats))


@admin.route("/logs")
def logs() -> Response:
    page = request.args.get("page", 1, type=int)
    logs = Log.query.order_by(Log.timestamp.desc()).paginate(page=page, per_page=50)
    return cast(Response, render_template("admin/logs.html", logs=logs))


@admin.route("/users")
@login_required
@admin_required
def users() -> Response:
    try:
        users = User.query.all()
        return cast(Response, render_template("admin/users.html", users=users))
    except Exception:
        flash("Произошла ошибка при загрузке пользователей", "error")
        return redirect(url_for("admin.index"))


@admin.route("/user/<int:id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_user(id: int) -> Response:
    try:
        user = User.query.get_or_404(id)
        if user.id == current_user.id:
            flash("Вы не можете удалить свой аккаунт", "error")
            return redirect(url_for("admin.users"))
        db.session.delete(user)
        db.session.commit()
        flash("Пользователь успешно удален", "success")
    except Exception:
        db.session.rollback()
        flash("Произошла ошибка при удалении пользователя", "error")
    return redirect(url_for("admin.users"))


@admin.route("/services")
@login_required
@admin_required
def services() -> Response:
    try:
        services = Service.query.all()
        return cast(Response, render_template("admin/services.html", services=services))
    except Exception:
        flash("Произошла ошибка при загрузке услуг", "error")
        return redirect(url_for("admin.index"))


@admin.route("/service/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_service() -> Response:
    try:
        if request.method == "POST":
            flash("Услуга успешно создана", "success")
            return redirect(url_for("admin.services"))
        return cast(Response, render_template("admin/service_form.html"))
    except Exception:
        flash("Произошла ошибка при создании услуги", "error")
        return redirect(url_for("admin.services"))


@admin.route("/service/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_service(id: int) -> Response:
    try:
        service = Service.query.get_or_404(id)
        if request.method == "POST":
            flash("Услуга успешно обновлена", "success")
            return redirect(url_for("admin.services"))
        return cast(Response, render_template("admin/service_form.html", service=service))
    except Exception:
        flash("Произошла ошибка при редактировании услуги", "error")
        return redirect(url_for("admin.services"))


@admin.route("/service/<int:id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_service(id: int) -> Response:
    try:
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        flash("Услуга успешно удалена", "success")
    except Exception:
        db.session.rollback()
        flash("Произошла ошибка при удалении услуги", "error")
    return redirect(url_for("admin.services"))
