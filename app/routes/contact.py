from typing import cast

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import SQLAlchemyError

from app import limiter  # Используем глобальный limiter
from app import db
from app.models.contact import ContactMessage

bp = Blueprint("contact", __name__)


@bp.route("/contact", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def index() -> str:
    """Handle contact form."""
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            message = request.form.get("message")

            contact_message = ContactMessage(name=name, email=email, message=message)
            db.session.add(contact_message)
            db.session.commit()

            flash("Your message has been sent successfully!", "success")
            return cast(str, redirect(url_for("public.index")))
        except SQLAlchemyError:
            flash("Error sending message", "error")
            return cast(str, render_template("contact/index.html"))

    return cast(str, render_template("contact/index.html"))
