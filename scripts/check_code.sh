#!/bin/bash

# Проверка форматирования кода
echo "Running Black..."
black . --check

# Проверка импортов
echo "Running isort..."
isort . --check-only

# Проверка линтером
echo "Running Flake8..."
flake8 .

# Проверка типов
echo "Running MyPy..."
mypy . 