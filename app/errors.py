from typing import Any, Dict, Tuple, Union

from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import (
    BadRequest,
    Forbidden,
    HTTPException,
    InternalServerError,
    MethodNotAllowed,
    NotFound,
    TooManyRequests,
    Unauthorized,
)


def init_error_handlers(app: Flask) -> None:
    register_client_errors(app)
    register_rate_limit_and_method_errors(app)
    register_server_errors(app)


def register_client_errors(app: Flask) -> None:
    @app.errorhandler(BadRequest)
    def bad_request_error(error: BadRequest) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)

    @app.errorhandler(Unauthorized)
    def unauthorized_error(error: Unauthorized) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)

    @app.errorhandler(Forbidden)
    def forbidden_error(error: Forbidden) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)

    @app.errorhandler(NotFound)
    def not_found_error(error: NotFound) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)


def register_rate_limit_and_method_errors(app: Flask) -> None:
    @app.errorhandler(MethodNotAllowed)
    def method_not_allowed_error(error: MethodNotAllowed) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)

    @app.errorhandler(TooManyRequests)
    def too_many_requests_error(error: TooManyRequests) -> Tuple[Union[str, Dict[str, Any]], int]:
        return handle_error(error)


def register_server_errors(app: Flask) -> None:
    from app import db  # 👈 Переносим импорт внутрь

    @app.errorhandler(InternalServerError)
    def internal_error(error: InternalServerError) -> Tuple[Union[str, Dict[str, Any]], int]:
        db.session.rollback()
        return handle_error(error)

    @app.errorhandler(Exception)
    def unhandled_exception(error: Exception) -> Tuple[Union[str, Dict[str, Any]], int]:
        db.session.rollback()
        if isinstance(error, HTTPException):
            return handle_error(error)
        return jsonify({"error": "Internal Server Error"}), 500


def handle_error(error: HTTPException) -> Tuple[Union[str, Dict[str, Any]], int]:
    status_code = error.code or 500
    if request.path.startswith("/api/"):
        return jsonify({"error": str(error)}), status_code
    return render_template("errors/error.html", error=error), status_code
