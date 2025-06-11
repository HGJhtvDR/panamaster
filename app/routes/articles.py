from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Article, Category

articles = Blueprint('articles', __name__)

@articles.route('/articles')
def index():
    try:
        page = request.args.get('page', 1, type=int)
        articles = Article.query.filter_by(published=True).paginate(page=page, per_page=10)
        return render_template('public/articles.html', articles=articles)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке статей', 'error')
        return redirect(url_for('public.index'))

@articles.route('/articles/<string:slug>')
def show(slug):
    try:
        article = Article.query.filter_by(slug=slug, published=True).first_or_404()
        return render_template('public/article.html', article=article)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке статьи', 'error')
        return redirect(url_for('articles.index'))

@articles.route('/articles/category/<string:category>')
def category(category):
    try:
        page = request.args.get('page', 1, type=int)
        category = Category.query.filter_by(slug=category).first_or_404()
        articles = Article.query.filter_by(category_id=category.id, published=True).paginate(page=page, per_page=10)
        return render_template('public/articles.html', articles=articles, category=category)
    except SQLAlchemyError as e:
        flash('Произошла ошибка при загрузке статей категории', 'error')
        return redirect(url_for('articles.index')) 