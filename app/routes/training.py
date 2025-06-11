from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Course, Training

training = Blueprint('training', __name__)

@training.route('/training')
def index():
    try:
        courses = Course.query.filter_by(published=True).all()
        return render_template('public/training.html', courses=courses)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке курсов', 'error')
        return redirect(url_for('public.index'))

@training.route('/training/<int:id>')
def show_course(id):
    try:
        course = Course.query.get_or_404(id)
        return render_template('public/course.html', course=course)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке курса', 'error')
        return redirect(url_for('training.index'))

@training.route('/training/register/<int:id>', methods=['GET', 'POST'])
@login_required
def register(id):
    try:
        course = Course.query.get_or_404(id)
        if request.method == 'POST':
            training = Training(
                user_id=current_user.id,
                course_id=course.id,
                status='pending'
            )
            db.session.add(training)
            db.session.commit()
            flash('Вы успешно зарегистрировались на курс', 'success')
            return redirect(url_for('training.show_course', id=course.id))
        return render_template('public/training_register.html', course=course)
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('Произошла ошибка при регистрации на курс', 'error')
        return redirect(url_for('training.index')) 