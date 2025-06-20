from typing import cast

from flask import Blueprint, render_template
from flask.wrappers import Response

bp = Blueprint("public", __name__)


@bp.route("/", methods=["GET"])
def index() -> str | Response:
    """Show the main page."""
    return cast(str, render_template("public/index.html"))


@bp.route("/about", methods=["GET"])
def about() -> str | Response:
    """Show the about page."""
    return cast(str, render_template("public/about.html"))


@bp.route("/company")
def company() -> str | Response:
    return render_template("public/company.html")


@bp.route("/services")
def services() -> str | Response:
    return render_template("public/services.html")


@bp.route("/contact", methods=["GET"])
def contact() -> str | Response:
    """Show the contact page."""
    return cast(str, render_template("public/contact.html"))


@bp.route("/partners")
def partners() -> str | Response:
    return render_template("public/partners.html")


__all__ = ["bp"]
