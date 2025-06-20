from typing import cast

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, logout_user
from werkzeug.wrappers import Response

from ..forms import RegistrationForm
from . import auth


@auth.route("/login")
def login() -> Response:
    """Отображение формы входа."""
    return cast(Response, render_template("auth/login.html"))


@auth.route("/register", methods=["GET", "POST"])
def register() -> Response:
    """Обработка регистрации пользователя."""
    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: Добавить создание пользователя
        flash("Регистрация успешна! Теперь вы можете войти.", "success")
        return redirect(url_for("auth.login"))
    return cast(Response, render_template("auth/register.html", form=form))


@auth.route("/logout")
@login_required
def logout() -> Response:
    """Выход из системы."""
    logout_user()
    return redirect(url_for("main.index"))
