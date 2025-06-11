from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Job, JobApplication

jobs = Blueprint('jobs', __name__)

@jobs.route('/jobs')
def index():
    try:
        page = request.args.get('page', 1, type=int)
        jobs = Job.query.filter_by(active=True).paginate(page=page, per_page=10)
        return render_template('public/jobs.html', jobs=jobs)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке вакансий', 'error')
        return redirect(url_for('public.index'))

@jobs.route('/jobs/<int:id>')
def show(id):
    try:
        job = Job.query.get_or_404(id)
        return render_template('public/job.html', job=job)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке вакансии', 'error')
        return redirect(url_for('jobs.index'))

@jobs.route('/jobs/apply/<int:id>', methods=['GET', 'POST'])
@login_required
def apply(id):
    try:
        job = Job.query.get_or_404(id)
        if request.method == 'POST':
            application = JobApplication(
                job_id=job.id,
                user_id=current_user.id,
                status='pending'
            )
            db.session.add(application)
            db.session.commit()
            flash('Ваша заявка успешно отправлена', 'success')
            return redirect(url_for('jobs.show', id=job.id))
        return render_template('public/job_apply.html', job=job)
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('Произошла ошибка при отправке заявки', 'error')
        return redirect(url_for('jobs.index')) 