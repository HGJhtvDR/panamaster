#!/bin/bash

# Обновляем систему
sudo apt update
sudo apt upgrade -y

# Устанавливаем необходимые пакеты
sudo apt install -y python3-venv python3-dev nginx supervisor

# Создаем директорию для проекта
sudo mkdir -p /var/www/panamaster
sudo chown -R $USER:$USER /var/www/panamaster

# Копируем файлы проекта
cp -r * /var/www/panamaster/

# Создаем виртуальное окружение
cd /var/www/panamaster
python3 -m venv venv
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt
pip install gunicorn

# Создаем директорию для логов
mkdir -p logs

# Копируем конфигурацию nginx
sudo cp nginx/panamaster /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/panamaster /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# Копируем systemd сервис
sudo cp panamaster.service /etc/systemd/system/

# Перезапускаем сервисы
sudo systemctl daemon-reload
sudo systemctl start panamaster
sudo systemctl enable panamaster
sudo systemctl restart nginx

# Настраиваем права доступа
sudo chown -R www-data:www-data /var/www/panamaster
sudo chmod -R 755 /var/www/panamaster

# Создаем директорию для загрузок
sudo mkdir -p /var/www/panamaster/uploads
sudo chown -R www-data:www-data /var/www/panamaster/uploads

echo "Установка завершена!"
echo "Для настройки SSL выполните: ./install_ssl.sh" 