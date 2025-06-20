from typing import cast

from flask import Blueprint, flash, redirect, render_template, url_for
from sqlalchemy.exc import SQLAlchemyError

from app.models.service import Service

bp = Blueprint("services", __name__)


@bp.route("/services")
def index() -> str:
    """Show all services."""
    try:
        services = Service.query.all()
        return cast(str, render_template("services/index.html", services=services))
    except SQLAlchemyError:
        flash("Error loading services", "error")
        return cast(str, render_template("services/index.html", services=[]))


@bp.route("/services/<int:service_id>")
def show(service_id: int) -> str:
    """Show a specific service."""
    try:
        service = Service.query.get_or_404(service_id)
        return cast(str, render_template("services/show.html", service=service))
    except SQLAlchemyError:
        flash("Error loading service", "error")
        return cast(str, redirect(url_for("services.index")))
