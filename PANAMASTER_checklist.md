
# ✅ Чек-лист по подготовке среды разработки сайта PANAMASTER

## 📁 Структура проекта

- [x] `project_root/`
- [x] `app/` с модулями `routes`, `models`, `services`, `templates`, `static`
- [x] `static/` содержит `css/`, `js/`, `images/`
- [x] `templates/` содержит `base.html`, `index.html`
- [x] `config/` содержит `base.py`, `dev.py`, `prod.py`, `.env`
- [x] `database/` и `Flask-Migrate` для миграций

## ⚙️ Зависимости (Python)

- [x] Flask
- [x] Flask-WTF (для CSRF-защиты форм)
- [x] Flask-Migrate (для миграций БД)
- [x] Flask-SQLAlchemy
- [x] python-dotenv
- [x] psycopg2 (PostgreSQL драйвер)
- [x] pytest (для тестирования)

## 🐘 PostgreSQL

- [x] Установлен PostgreSQL на сервере Ubuntu
- [x] Создана база данных для проекта
- [x] Настроено подключение через `SQLALCHEMY_DATABASE_URI`
- [x] pgAdmin доступен для мониторинга

## 🐳 Docker (по желанию)

- [x] Установлен Docker + WSL2 (если Windows)
- [x] Настроен `Dockerfile` и `docker-compose.yml`
- [x] Используется PostgreSQL, Flask, Nginx в контейнерах

## 🔐 Безопасность

- [x] CSRF-защита через Flask-WTF
- [x] Валидация форм и загрузок
- [x] Параметризованные SQL-запросы
- [x] .env не попадает в git (`.gitignore`)
- [x] SSL-подключение к базе (опционально)
- [x] Настроены роли и права в базе

## 🌐 SEO и структура сайта

- [x] `sitemap.xml` с многоязычными версиями (ru/en)
- [x] `robots.txt` с доступом для Google и Yandex
- [x] `<meta name="robots">`, OpenGraph и мета-теги
- [x] Подключение к Яндекс.Вебмастер и Google Search Console

## ✅ Дополнительно

- [x] `README.md` проекта с инструкцией по запуску
- [x] Командный интерфейс для деплоя (bash, Fabric или Ansible)
- [x] `tests/` с `pytest` и примерами
