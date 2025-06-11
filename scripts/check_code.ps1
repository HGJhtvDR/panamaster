# Проверка форматирования кода
Write-Host "Running Black..."
black . --check

# Проверка импортов
Write-Host "Running isort..."
isort . --check-only

# Проверка линтером
Write-Host "Running Flake8..."
flake8 .

# Проверка типов
Write-Host "Running MyPy..."
mypy . 