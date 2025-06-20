from typing import Union

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.wrappers import Response as WerkzeugResponse

from app import db
from app.models.training import Course, Training

ResponseType = Union[str, WerkzeugResponse]

training = Blueprint("training", __name__)


@training.route("/training")
def index() -> ResponseType:
    try:
        courses = Course.query.all()
    except SQLAlchemyError:
        flash("Ошибка при загрузке курсов", "error")
        courses = []
    return render_template("training/index.html", courses=courses)


@training.route("/training/<int:course_id>")
def show(course_id: int) -> ResponseType:
    try:
        course = Course.query.get_or_404(course_id)
        return render_template("training/show.html", course=course)
    except SQLAlchemyError:
        flash("Ошибка при загрузке курса", "error")
        return redirect(url_for("training.index"))


@training.route("/training/register/<int:id>", methods=["GET", "POST"])
@login_required
def register(id: int) -> ResponseType:
    try:
        course = Course.query.get_or_404(id)
        if request.method == "POST":
            db.session.add(Training(user_id=current_user.id, course_id=course.id, status="pending"))
            db.session.commit()
            flash("Вы успешно зарегистрировались на курс", "success")
            return redirect(url_for("training.show", course_id=course.id))
        return render_template("public/training_register.html", course=course)
    except SQLAlchemyError:
        db.session.rollback()
        flash("Произошла ошибка при регистрации на курс", "error")
        return redirect(url_for("training.index"))


@training.route("/training/<int:course_id>/enroll", methods=["POST"])
def enroll(course_id: int) -> WerkzeugResponse:
    try:
        db.session.add(Training(course_id=course_id))
        db.session.commit()
        flash("Вы успешно записались на курс", "success")
    except SQLAlchemyError:
        db.session.rollback()
        flash("Произошла ошибка при записи на курс", "error")
    return redirect(url_for("training.show", course_id=course_id))


@training.route("/training/category/<category>")
def category(category: str) -> ResponseType:
    try:
        courses = Course.query.filter_by(category=category).all()
    except SQLAlchemyError:
        flash("Ошибка при загрузке курсов по категории", "error")
        courses = []
    return render_template("training/category.html", courses=courses, category=category)
