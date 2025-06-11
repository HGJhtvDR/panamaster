from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask_principal import Permission, RoleNeed

from app import db
from app.models.article import Article
from app.models.service import Service
from app.models.user import User
from app.models import Course, Job, Project, Category, Product, Portfolio, Knowledge, Log

from . import admin

# Определение разрешений
admin_permission = Permission(RoleNeed('admin'))

@admin.before_request
@login_required
@admin_permission.require()
def before_request():
    """Проверка прав доступа перед каждым запросом"""
    pass

def admin_required(f):
    """Декоратор для проверки прав администратора"""
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("У вас нет доступа к этой странице", "error")
            return redirect(url_for("public.index"))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function


@admin.route("/")
@login_required
@admin_required
def index():
    """Главная страница админ-панели"""
    return render_template("admin/index.html")


@admin.route("/dashboard")
def dashboard():
    """Панель управления"""
    stats = {
        'users': User.query.count(),
        'services': Service.query.count(),
        'articles': Article.query.count(),
        'courses': Course.query.count(),
        'jobs': Job.query.count(),
        'projects': Project.query.count(),
        'categories': Category.query.count(),
        'products': Product.query.count(),
        'portfolios': Portfolio.query.count(),
        'knowledge': Knowledge.query.count()
    }
    return render_template('admin/dashboard.html', stats=stats)


@admin.route("/logs")
def logs():
    """Просмотр логов"""
    page = request.args.get('page', 1, type=int)
    logs = Log.query.order_by(Log.timestamp.desc()).paginate(page=page, per_page=50)
    return render_template('admin/logs.html', logs=logs)


@admin.route("/users")
@login_required
@admin_required
def users():
    try:
        users = User.query.all()
        return render_template("admin/users.html", users=users)
    except Exception as e:
        flash("Произошла ошибка при загрузке пользователей", "error")
        return redirect(url_for("admin.index"))


@admin.route("/user/<int:id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        if user.id == current_user.id:
            flash("Вы не можете удалить свой аккаунт", "error")
            return redirect(url_for("admin.users"))
        db.session.delete(user)
        db.session.commit()
        flash("Пользователь успешно удален", "success")
    except Exception as e:
        db.session.rollback()
        flash("Произошла ошибка при удалении пользователя", "error")
    return redirect(url_for("admin.users"))


@admin.route("/services")
@login_required
@admin_required
def services():
    try:
        services = Service.query.all()
        return render_template("admin/services.html", services=services)
    except Exception as e:
        flash("Произошла ошибка при загрузке услуг", "error")
        return redirect(url_for("admin.index"))


@admin.route("/service/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_service():
    try:
        if request.method == "POST":
            # Здесь будет логика создания услуги
            flash("Услуга успешно создана", "success")
            return redirect(url_for("admin.services"))
        return render_template("admin/service_form.html")
    except Exception as e:
        flash("Произошла ошибка при создании услуги", "error")
        return redirect(url_for("admin.services"))


@admin.route("/service/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_service(id):
    try:
        service = Service.query.get_or_404(id)
        if request.method == "POST":
            # Здесь будет логика редактирования услуги
            flash("Услуга успешно обновлена", "success")
            return redirect(url_for("admin.services"))
        return render_template("admin/service_form.html", service=service)
    except Exception as e:
        flash("Произошла ошибка при редактировании услуги", "error")
        return redirect(url_for("admin.services"))


@admin.route("/service/<int:id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_service(id):
    try:
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        flash("Услуга успешно удалена", "success")
    except Exception as e:
        db.session.rollback()
        flash("Произошла ошибка при удалении услуги", "error")
    return redirect(url_for("admin.services"))


@admin.route("/articles")
@login_required
@admin_required
def articles():
    try:
        articles = Article.query.all()
        return render_template("admin/articles.html", articles=articles)
    except Exception as e:
        flash("Произошла ошибка при загрузке статей", "error")
        return redirect(url_for("admin.index"))


@admin.route("/article/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_article():
    try:
        if request.method == "POST":
            # Здесь будет логика создания статьи
            flash("Статья успешно создана", "success")
            return redirect(url_for("admin.articles"))
        return render_template("admin/article_form.html")
    except Exception as e:
        flash("Произошла ошибка при создании статьи", "error")
        return redirect(url_for("admin.articles"))


@admin.route("/article/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_article(id):
    try:
        article = Article.query.get_or_404(id)
        if request.method == "POST":
            # Здесь будет логика редактирования статьи
            flash("Статья успешно обновлена", "success")
            return redirect(url_for("admin.articles"))
        return render_template("admin/article_form.html", article=article)
    except Exception as e:
        flash("Произошла ошибка при редактировании статьи", "error")
        return redirect(url_for("admin.articles"))


@admin.route("/article/<int:id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_article(id):
    try:
        article = Article.query.get_or_404(id)
        db.session.delete(article)
        db.session.commit()
        flash("Статья успешно удалена", "success")
    except Exception as e:
        db.session.rollback()
        flash("Произошла ошибка при удалении статьи", "error")
    return redirect(url_for("admin.articles"))
