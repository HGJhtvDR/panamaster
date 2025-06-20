from typing import Union

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.wrappers import Response as WerkzeugResponse

from app import db
from app.models.user import User

bp = Blueprint("auth", __name__)
ResponseType = Union[str, WerkzeugResponse]


@bp.route("/login", methods=["GET", "POST"])
def login() -> ResponseType:
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.index"))

        flash("Invalid username or password", "error")

    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout() -> WerkzeugResponse:
    """Handle user logout."""
    logout_user()
    flash("Вы успешно вышли из системы", "success")
    return redirect(url_for("main.index"))


@bp.route("/register", methods=["GET", "POST"])
def register() -> ResponseType:
    """Handle user registration."""
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
            return render_template("auth/register.html")

        try:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("main.index"))
        except SQLAlchemyError:
            db.session.rollback()
            flash("Error creating user", "error")
            return render_template("auth/register.html")

    return render_template("auth/register.html")
