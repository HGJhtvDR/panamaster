from typing import cast

from flask import Blueprint, flash, redirect, render_template, url_for
from werkzeug.wrappers import Response

bp = Blueprint("company", __name__)


@bp.route("/company", methods=["GET"])
def index() -> Response:
    """Show company information."""
    try:
        return cast(Response, render_template("company/index.html"))
    except Exception:
        flash("Произошла ошибка при загрузке страницы", "error")
        return redirect(url_for("public.index"))


@bp.route("/company/about", methods=["GET"])
def about() -> Response:
    """Show about page."""
    try:
        return cast(Response, render_template("company/about.html"))
    except Exception:
        flash("Произошла ошибка при загрузке страницы", "error")
        return redirect(url_for("company.index"))


@bp.route("/company/team", methods=["GET"])
def team() -> Response:
    """Show team page."""
    try:
        return cast(Response, render_template("company/team.html"))
    except Exception:
        flash("Произошла ошибка при загрузке страницы", "error")
        return redirect(url_for("company.index"))


@bp.route("/company/certificates")
def certificates() -> Response:
    """Show certificates page."""
    try:
        return cast(Response, render_template("public/certificates.html"))
    except Exception:
        flash("Произошла ошибка при загрузке страницы", "error")
        return redirect(url_for("company.index"))


@bp.route("/company/careers", methods=["GET"])
def careers() -> Response:
    """Show careers page."""
    return cast(Response, render_template("company/careers.html"))
