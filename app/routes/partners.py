from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Partner, PartnerRequest

partners = Blueprint('partners', __name__)

def partner_token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            flash('Требуется токен доступа', 'error')
            return redirect(url_for('public.index'))
            
        partner = Partner.query.filter_by(token=token, active=True).first()
        if not partner:
            flash('Недействительный токен', 'error')
            return redirect(url_for('public.index'))
            
        return f(partner, *args, **kwargs)
    return decorated_function

@partners.route('/partners')
def index():
    try:
        partners = Partner.query.filter_by(active=True).all()
        return render_template('public/partners.html', partners=partners)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке партнеров', 'error')
        return redirect(url_for('public.index'))

@partners.route('/partners/request', methods=['GET', 'POST'])
@login_required
def request_partnership():
    try:
        if request.method == 'POST':
            request = PartnerRequest(
                user_id=current_user.id,
                company_name=request.form.get('company_name'),
                contact_name=request.form.get('contact_name'),
                email=request.form.get('email'),
                phone=request.form.get('phone'),
                message=request.form.get('message')
            )
            db.session.add(request)
            db.session.commit()
            flash('Ваша заявка успешно отправлена', 'success')
            return redirect(url_for('partners.index'))
        return render_template('public/partner_request.html')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('Произошла ошибка при отправке заявки', 'error')
        return redirect(url_for('partners.index'))

@partners.route('/partners/portal/<string:partner>')
@login_required
def portal(partner):
    try:
        partner = Partner.query.filter_by(slug=partner, active=True).first_or_404()
        if not partner.is_authorized(current_user):
            flash('У вас нет доступа к порталу партнера', 'error')
            return redirect(url_for('partners.index'))
        return render_template('public/partner_portal.html', partner=partner)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке портала партнера', 'error')
        return redirect(url_for('partners.index')) 