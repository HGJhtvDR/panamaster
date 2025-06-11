import pytest
from flask import url_for


def test_index_page(client):
    """Тест главной страницы"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Panamaster" in response.data
    assert (
        b"\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f" in response.data
    )  # "Главная" в UTF-8


def test_company_page(client):
    """Тест страницы о компании"""
    response = client.get("/company")
    assert response.status_code == 200
    assert (
        b"\xd0\x9e \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8"
        in response.data
    )  # "О компании" в UTF-8


def test_services_page(client):
    """Тест страницы услуг"""
    response = client.get("/services")
    assert response.status_code == 200
    assert (
        b"\xd0\xa3\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8" in response.data
    )  # "Услуги" в UTF-8


def test_contact_page(client):
    """Тест страницы контактов"""
    response = client.get("/contact")
    assert response.status_code == 200
    assert (
        b"\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd1\x8b"
        in response.data
    )  # "Контакты" в UTF-8
