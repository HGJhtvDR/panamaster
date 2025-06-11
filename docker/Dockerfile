FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Создание необходимых директорий
RUN mkdir -p uploads/portfolio uploads/knowledge_attachments uploads/diagnostics

# Установка прав доступа
RUN chown -R nobody:nogroup /app

# Переключение на непривилегированного пользователя
USER nobody

# Запуск приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"] 