#!/bin/bash

# Устанавливаем Certbot
sudo apt install -y certbot python3-certbot-nginx

# Получаем SSL сертификат
sudo certbot --nginx -d panamaster.ru -d www.panamaster.ru

# Проверяем автоматическое обновление сертификата
sudo certbot renew --dry-run 