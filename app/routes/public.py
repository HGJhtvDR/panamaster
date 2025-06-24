from flask import Blueprint

bp = Blueprint("public", __name__)


@bp.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Panamaster - Промышленный сервис</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Arial', sans-serif;
                background-color: #ffffff;
                color: #333333;
                line-height: 1.6;
            }

            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 40px;
                background-color: #ffffff;
                border-bottom: 1px solid #e0e0e0;
                max-width: 1400px;
                margin: 0 auto;
            }

            .logo {
                font-size: 28px;
                font-weight: 300;
                letter-spacing: 2px;
                color: #333333;
                text-decoration: none;
            }

            .center-text {
                font-size: 14px;
                font-weight: 400;
                color: #666666;
                letter-spacing: 1px;
            }

            .contact-info {
                display: flex;
                align-items: center;
                gap: 15px;
            }

            .phone-link {
                color: #333333;
                text-decoration: none;
                font-size: 14px;
                font-weight: 400;
                letter-spacing: 0.5px;
            }

            .phone-link:hover {
                color: #666666;
            }

            .whatsapp-link {
                display: inline-block;
                width: 24px;
                height: 24px;
                background-color: #25D366;
                border-radius: 50%;
                text-align: center;
                line-height: 24px;
                color: white;
                text-decoration: none;
                font-size: 14px;
            }

            .main-content {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 60vh;
                text-align: center;
            }

            .development-text {
                font-size: 24px;
                font-weight: 300;
                color: #666666;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <header class="header">
            <div class="logo">PANAMASTER</div>
            <div class="center-text">ПРОМЫШЛЕННЫЙ СЕРВИС</div>
            <div class="contact-info">
                <a href="tel:+79265250545" class="phone-link">+7 (926) 525-05-45</a>
                <a href="https://wa.me/79265250545" class="whatsapp-link" target="_blank">W</a>
            </div>
        </header>

        <main class="main-content">
            <div class="development-text">Сайт в разработке</div>
        </main>
    </body>
    </html>
    """


__all__ = ["bp"]
