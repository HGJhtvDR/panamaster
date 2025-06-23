import os

from app import create_app

# Определение среды запуска из переменной окружения
env = os.getenv("FLASK_ENV", "production")

# Создание приложения с нужной конфигурацией
app = create_app(env)

if __name__ == "__main__":
    debug_mode = env == "development"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
