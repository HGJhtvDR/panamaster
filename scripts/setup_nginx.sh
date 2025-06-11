#!/bin/bash

# Проверка прав суперпользователя
if [ "$EUID" -ne 0 ]; then 
    echo "Пожалуйста, запустите скрипт с правами суперпользователя"
    exit 1
fi

# Установка Nginx
echo "Установка Nginx..."
apt-get update
apt-get install -y nginx

# Создание директорий
echo "Создание необходимых директорий..."
mkdir -p /var/www/panamaster
mkdir -p /var/log/nginx/panamaster

# Копирование конфигурации
echo "Копирование конфигурации Nginx..."
cp nginx/panamaster.conf /etc/nginx/sites-available/panamaster

# Создание символической ссылки
echo "Создание символической ссылки..."
ln -sf /etc/nginx/sites-available/panamaster /etc/nginx/sites-enabled/

# Удаление дефолтной конфигурации
echo "Удаление дефолтной конфигурации..."
rm -f /etc/nginx/sites-enabled/default

# Проверка конфигурации
echo "Проверка конфигурации Nginx..."
nginx -t

# Перезапуск Nginx
echo "Перезапуск Nginx..."
systemctl restart nginx

# Установка SSL сертификатов (если нужно)
echo "Хотите установить SSL сертификаты? (y/n)"
read -r install_ssl

if [ "$install_ssl" = "y" ]; then
    echo "Установка Certbot..."
    apt-get install -y certbot python3-certbot-nginx
    
    echo "Введите доменное имя (например, panamaster.com):"
    read -r domain_name
    
    echo "Получение SSL сертификата..."
    certbot --nginx -d "$domain_name" -d "www.$domain_name"
fi

echo "Настройка Nginx завершена!" 