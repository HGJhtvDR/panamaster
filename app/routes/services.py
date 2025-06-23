from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.wrappers import Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from sqlalchemy.exc import SQLAlchemyError

from app.models.service import Service  # Убедись, что модель действительно здесь

services = Blueprint("services", __name__)
limiter = Limiter(key_func=get_remote_address)


@services.route("/services")
def index() -> Response:
    try:
        services_list = Service.query.all()
        return render_template("public/services.html", services=services_list)
    except SQLAlchemyError:
        flash("Произошла ошибка при загрузке услуг", "error")
        return redirect(url_for("public.index"))


@services.route("/service/<int:id>")
def show(id: int) -> Response:
    try:
        service = Service.query.get_or_404(id)
        return render_template("public/service.html", service=service)
    except SQLAlchemyError:
        flash("Произошла ошибка при загрузке услуги", "error")
        return redirect(url_for("services.index"))
