from flask import Blueprint, render_template

company = Blueprint('company', __name__)

@company.route('/company')
def index():
    try:
        return render_template('public/company.html')
    except Exception as e:
        flash('Произошла ошибка при загрузке страницы', 'error')
        return redirect(url_for('public.index'))

@company.route('/company/about')
def about():
    try:
        return render_template('public/about.html')
    except Exception as e:
        flash('Произошла ошибка при загрузке страницы', 'error')
        return redirect(url_for('company.index'))

@company.route('/company/team')
def team():
    try:
        return render_template('public/team.html')
    except Exception as e:
        flash('Произошла ошибка при загрузке страницы', 'error')
        return redirect(url_for('company.index'))

@company.route('/company/certificates')
def certificates():
    try:
        return render_template('public/certificates.html')
    except Exception as e:
        flash('Произошла ошибка при загрузке страницы', 'error')
        return redirect(url_for('company.index')) 