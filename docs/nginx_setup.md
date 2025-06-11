# Установка и настройка Nginx

## Требования
- Ubuntu/Debian Linux
- Права суперпользователя
- Доменное имя (для SSL)

## Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/yourusername/panamaster.git
cd panamaster
```

2. Сделайте скрипт установки исполняемым:
```bash
chmod +x scripts/setup_nginx.sh
```

3. Запустите скрипт установки:
```bash
sudo ./scripts/setup_nginx.sh
```

## Ручная установка

Если вы предпочитаете установить Nginx вручную, выполните следующие шаги:

1. Установите Nginx:
```bash
sudo apt-get update
sudo apt-get install nginx
```

2. Создайте необходимые директории:
```bash
sudo mkdir -p /var/www/panamaster
sudo mkdir -p /var/log/nginx/panamaster
```

3. Скопируйте конфигурацию:
```bash
sudo cp nginx/panamaster.conf /etc/nginx/sites-available/panamaster
```

4. Создайте символическую ссылку:
```bash
sudo ln -sf /etc/nginx/sites-available/panamaster /etc/nginx/sites-enabled/
```

5. Удалите дефолтную конфигурацию:
```bash
sudo rm -f /etc/nginx/sites-enabled/default
```

6. Проверьте конфигурацию:
```bash
sudo nginx -t
```

7. Перезапустите Nginx:
```bash
sudo systemctl restart nginx
```

## Настройка SSL

Для настройки SSL с помощью Let's Encrypt:

1. Установите Certbot:
```bash
sudo apt-get install certbot python3-certbot-nginx
```

2. Получите сертификат:
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## Проверка установки

1. Проверьте статус Nginx:
```bash
sudo systemctl status nginx
```

2. Проверьте доступность сайта:
```bash
curl -I http://yourdomain.com
```

## Устранение неполадок

1. Проверка логов:
```bash
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/panamaster/error.log
```

2. Проверка конфигурации:
```bash
sudo nginx -t
```

3. Перезапуск Nginx:
```bash
sudo systemctl restart nginx
```

## Обновление конфигурации

При внесении изменений в конфигурацию:

1. Проверьте синтаксис:
```bash
sudo nginx -t
```

2. Перезагрузите конфигурацию:
```bash
sudo nginx -s reload
```

## Безопасность

- Регулярно обновляйте Nginx:
```bash
sudo apt-get update
sudo apt-get upgrade nginx
```

- Проверяйте логи на наличие подозрительной активности
- Используйте только последние версии SSL/TLS
- Регулярно обновляйте SSL сертификаты

## Дополнительные ресурсы

- [Официальная документация Nginx](https://nginx.org/en/docs/)
- [Let's Encrypt документация](https://letsencrypt.org/docs/)
- [Certbot документация](https://certbot.eff.org/docs/) 