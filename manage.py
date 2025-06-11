#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from flask.cli import FlaskGroup

from app import create_app, db
from app.models import User


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "panamaster.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)


cli = FlaskGroup(create_app=create_app)


@cli.command("create_db")
def create_db():
    """Создает базу данных"""
    db.create_all()
    print("База данных создана")


@cli.command("drop_db")
def drop_db():
    """Удаляет базу данных"""
    db.drop_all()
    print("База данных удалена")


@cli.command("create_admin")
def create_admin():
    """Создает администратора"""
    from getpass import getpass

    email = input("Email: ")
    password = getpass("Password: ")
    admin = User(email=email, username="admin", is_admin=True)
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    print("Администратор создан")


if __name__ == "__main__":
    cli()
