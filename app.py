from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Создаем Blueprint для публичных страниц
public = Blueprint('public', __name__)

# Модели
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Маршруты
@public.route('/')
def index():
    return render_template('public/index.html')

@public.route('/services')
def services():
    services = Service.query.all()
    return render_template('public/services.html', services=services)

@public.route('/company')
def company():
    return render_template('public/company.html')

@public.route('/portfolio')
def portfolio():
    projects = Portfolio.query.order_by(Portfolio.created_at.desc()).all()
    return render_template('public/portfolio.html', projects=projects)

@public.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        
        contact = Contact(name=name, phone=phone, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        
        flash('Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.', 'success')
        return redirect(url_for('public.contact'))
    
    return render_template('public/contact.html')

@public.route('/articles')
def articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('public/articles.html', articles=articles)

@public.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('public/article.html', article=article)

# Обработка форм
@public.route('/callback', methods=['POST'])
def callback():
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    # Здесь можно добавить сохранение данных в базу
    print(f'Callback request from {name}, phone: {phone}')
    
    return {'status': 'success', 'message': 'Спасибо! Мы свяжемся с вами в ближайшее время.'}

# Регистрируем Blueprint
app.register_blueprint(public)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 