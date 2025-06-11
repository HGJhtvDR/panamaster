from flask import jsonify, request

from app import db
from app.models.article import Article
from app.models.service import Service

from . import api


@api.route("/services", methods=["GET"])
def get_services():
    services = Service.query.all()
    return jsonify(
        [
            {
                "id": service.id,
                "title": service.title,
                "description": service.description,
                "price": service.price,
            }
            for service in services
        ]
    )


@api.route("/services/<int:id>", methods=["GET"])
def get_service(id):
    service = Service.query.get_or_404(id)
    return jsonify(
        {
            "id": service.id,
            "title": service.title,
            "description": service.description,
            "price": service.price,
        }
    )


@api.route("/articles", methods=["GET"])
def get_articles():
    articles = Article.query.all()
    return jsonify(
        [
            {
                "id": article.id,
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at.isoformat(),
            }
            for article in articles
        ]
    )


@api.route("/articles/<int:id>", methods=["GET"])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify(
        {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at.isoformat(),
        }
    )
