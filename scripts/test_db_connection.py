from app import db, create_app
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print('Подключение к базе данных успешно!')
    except Exception as e:
        print(f'Ошибка подключения к базе данных: {e}') 