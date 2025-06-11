# Panamaster - Промышленный сервис

Веб-сайт компании, предоставляющей услуги по ремонту и обслуживанию промышленного оборудования.

## Особенности

- Современный адаптивный дизайн
- Формы обратной связи
- База данных для хранения заявок
- Административная панель
- Блог с новостями и статьями

## Технологии

- Python 3.8+
- Flask
- SQLAlchemy
- Bootstrap 5
- JavaScript
- SQLite

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/panamaster.git
cd panamaster
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте базу данных:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Запустите приложение:
```bash
python app.py
```

## Структура проекта

```
panamaster/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   └── public/
└── instance/
    └── site.db
```

## Лицензия

MIT 