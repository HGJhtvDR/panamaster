from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app import db
from app.models import Service

services = Blueprint('services', __name__)
limiter = Limiter(key_func=get_remote_address)

@services.route('/services')
def index():
    try:
        services = Service.query.all()
        return render_template('public/services.html', services=services)
    except Exception as e:
        flash('Произошла ошибка при загрузке услуг', 'error')
        return redirect(url_for('public.index'))

@services.route('/service/<int:id>')
def show(id):
    try:
        service = Service.query.get_or_404(id)
        return render_template('public/service.html', service=service)
    except Exception as e:
        flash('Произошла ошибка при загрузке услуги', 'error')
        return redirect(url_for('services.index')) 