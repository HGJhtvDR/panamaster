#!/bin/bash

# Форматирование кода
echo "Running Black..."
black .

# Сортировка импортов
echo "Running isort..."
isort .

# Автоматическое исправление ошибок линтера
echo "Running Flake8 with auto-fix..."
flake8 . --fix

# Проверка типов
echo "Running MyPy..."
mypy . 