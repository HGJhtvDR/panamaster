from flask_principal import Permission, RoleNeed
from flask_restful import Resource, reqparse

from app import db
from app.models import Article, User

# Парсеры для запросов
user_parser = reqparse.RequestParser()
user_parser.add_argument("username", type=str, required=True)
user_parser.add_argument("email", type=str, required=True)
user_parser.add_argument("password", type=str, required=True)

article_parser = reqparse.RequestParser()
article_parser.add_argument("title", type=str, required=True)
article_parser.add_argument("content", type=str, required=True)
article_parser.add_argument("author_id", type=int, required=True)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
        }

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        args = user_parser.parse_args()

        user.username = args["username"]
        user.email = args["email"]
        user.set_password(args["password"])

        db.session.commit()
        return {"message": "User updated successfully"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at.isoformat(),
            }
            for user in users
        ]

    def post(self):
        args = user_parser.parse_args()
        user = User(username=args["username"], email=args["email"])
        user.set_password(args["password"])

        db.session.add(user)
        db.session.commit()

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
        }, 201


class ArticleResource(Resource):
    def get(self, article_id):
        article = Article.query.get_or_404(article_id)
        return {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "author_id": article.author_id,
            "created_at": article.created_at.isoformat(),
        }

    def put(self, article_id):
        article = Article.query.get_or_404(article_id)
        args = article_parser.parse_args()

        article.title = args["title"]
        article.content = args["content"]
        article.author_id = args["author_id"]

        db.session.commit()
        return {"message": "Article updated successfully"}

    def delete(self, article_id):
        article = Article.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()
        return {"message": "Article deleted successfully"}


class ArticleListResource(Resource):
    def get(self):
        articles = Article.query.all()
        return [
            {
                "id": article.id,
                "title": article.title,
                "content": article.content,
                "author_id": article.author_id,
                "created_at": article.created_at.isoformat(),
            }
            for article in articles
        ]

    def post(self):
        args = article_parser.parse_args()
        article = Article(
            title=args["title"], content=args["content"], author_id=args["author_id"]
        )

        db.session.add(article)
        db.session.commit()

        return {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "author_id": article.author_id,
            "created_at": article.created_at.isoformat(),
        }, 201
