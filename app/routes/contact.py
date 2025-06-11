from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_limiter.util import get_remote_address

from app import db
from app.models import ContactMessage
from app import limiter  # Используем глобальный limiter

contact = Blueprint('contact', __name__)

@contact.route('/contact', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def index():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            
            if not all([name, email, message]):
                flash('Пожалуйста, заполните все поля', 'error')
                return redirect(url_for('contact.index'))
                
            contact_message = ContactMessage(
                name=name,
                email=email,
                message=message
            )
            db.session.add(contact_message)
            db.session.commit()
            
            flash('Ваше сообщение успешно отправлено', 'success')
            return redirect(url_for('contact.index'))
            
        return render_template('public/contact.html')
    except Exception as e:
        flash('Произошла ошибка при отправке сообщения', 'error')
        return redirect(url_for('contact.index')) 