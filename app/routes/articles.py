from typing import cast

from flask import Blueprint, render_template
from sqlalchemy.exc import SQLAlchemyError

from app.models.article import Article

bp = Blueprint("articles", __name__)


@bp.route("/articles")
def index() -> str:
    """Show all articles."""
    try:
        articles = Article.query.all()
        return cast(str, render_template("articles/index.html", articles=articles))
    except SQLAlchemyError:
        return cast(str, render_template("articles/index.html", articles=[]))


@bp.route("/articles/<int:article_id>")
def show(article_id: int) -> str:
    """Show a specific article."""
    try:
        article = Article.query.get_or_404(article_id)
        return cast(str, render_template("articles/show.html", article=article))
    except SQLAlchemyError:
        return cast(str, render_template("articles/index.html"))


@bp.route("/articles/category/<category>")
def category(category: str) -> str:
    """Show articles by category."""
    try:
        articles = Article.query.filter_by(category=category).all()
        return cast(str, render_template("articles/category.html", articles=articles, category=category))
    except SQLAlchemyError:
        return cast(str, render_template("articles/category.html", articles=[], category=category))
