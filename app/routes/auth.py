from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from app import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get("next")
                return redirect(next_page or url_for("public.index"))
            flash("Неверный email или пароль", "error")
        except Exception as e:
            flash("Произошла ошибка при входе", "error")
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Проверяем, не существует ли уже пользователь с таким email
            if User.query.filter_by(email=form.email.data).first():
                flash("Пользователь с таким email уже существует", "error")
                return render_template("auth/register.html", form=form)

            # Проверяем, не существует ли уже пользователь с таким именем
            if User.query.filter_by(username=form.username.data).first():
                flash("Пользователь с таким именем уже существует", "error")
                return render_template("auth/register.html", form=form)

            user = User(email=form.email.data, username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Регистрация успешна! Теперь вы можете войти.", "success")
            return redirect(url_for("auth.login"))
        except IntegrityError:
            db.session.rollback()
            flash("Произошла ошибка при регистрации. Возможно, такой email или имя пользователя уже существуют.", "error")
        except Exception as e:
            db.session.rollback()
            flash("Произошла ошибка при регистрации", "error")
    return render_template("auth/register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    try:
        logout_user()
        flash("Вы успешно вышли из системы", "success")
    except Exception as e:
        flash("Произошла ошибка при выходе из системы", "error")
    return redirect(url_for("public.index"))
