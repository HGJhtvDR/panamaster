# Форматирование кода
Write-Host "Running Black..."
black .

# Сортировка импортов
Write-Host "Running isort..."
isort .

# Автоматическое исправление ошибок линтера
Write-Host "Running Flake8 with auto-fix..."
flake8 . --fix

# Проверка типов
Write-Host "Running MyPy..."
mypy . 