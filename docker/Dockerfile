FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Создание нужных директорий
RUN mkdir -p uploads/portfolio uploads/knowledge_attachments uploads/diagnostics

# Запуск приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
