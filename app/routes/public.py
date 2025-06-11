from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.forms import ContactForm
from app.models.article import Article
from app.models.course import Course
from app.models.job import Job
from app.models.project import Project
from app.models.service import Service

public = Blueprint("public", __name__)


@public.route("/")
def index():
    return render_template("public/index.html")


@public.route("/company")
def company():
    return render_template("public/company.html")


@public.route("/services")
def services():
    try:
        services = Service.query.all()
        return render_template("public/services.html", services=services)
    except Exception as e:
        flash("Произошла ошибка при загрузке услуг", "error")
        return redirect(url_for("public.index"))


@public.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Здесь будет логика обработки формы
            flash("Ваше сообщение успешно отправлено!", "success")
            return redirect(url_for("public.contact"))
        except Exception as e:
            flash("Произошла ошибка при отправке сообщения", "error")
    return render_template("public/contact.html", form=form)


@public.route("/partners")
def partners():
    return render_template("public/partners.html")


@public.route("/jobs")
def jobs():
    try:
        jobs = Job.query.all()
        return render_template("public/jobs.html", jobs=jobs)
    except Exception as e:
        flash("Произошла ошибка при загрузке вакансий", "error")
        return redirect(url_for("public.index"))


@public.route("/articles")
def articles():
    try:
        page = request.args.get("page", 1, type=int)
        pagination = Article.query.order_by(Article.created_at.desc()).paginate(
            page=page, per_page=9, error_out=False
        )
        articles = pagination.items
        return render_template(
            "public/articles.html", articles=articles, pagination=pagination
        )
    except Exception as e:
        flash("Произошла ошибка при загрузке статей", "error")
        return redirect(url_for("public.index"))


@public.route("/article/<int:id>")
def article(id):
    try:
        article = Article.query.get_or_404(id)
        return render_template("public/article.html", article=article)
    except Exception as e:
        flash("Статья не найдена", "error")
        return redirect(url_for("public.articles"))


@public.route("/training")
def training():
    try:
        courses = Course.query.all()
        return render_template("public/training.html", courses=courses)
    except Exception as e:
        flash("Произошла ошибка при загрузке курсов", "error")
        return redirect(url_for("public.index"))


@public.route("/course/<int:id>")
def course_details(id):
    try:
        course = Course.query.get_or_404(id)
        return render_template("public/course.html", course=course)
    except Exception as e:
        flash("Курс не найден", "error")
        return redirect(url_for("public.training"))


@public.route("/portfolio")
def portfolio():
    try:
        projects = Project.query.all()
        return render_template("public/portfolio.html", projects=projects)
    except Exception as e:
        flash("Произошла ошибка при загрузке проектов", "error")
        return redirect(url_for("public.index"))
