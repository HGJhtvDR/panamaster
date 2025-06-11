# Магазин

Эта директория содержит каталог товаров с изображениями и метаданными.

## Структура

```
shop/
├── images/          # Изображения товаров
│   ├── products/    # Фотографии товаров
│   └── categories/  # Изображения категорий
└── data/           # Метаданные товаров
    ├── products.json
    └── categories.json
```

## Правила добавления товаров

1. Изображения должны быть в формате JPEG или PNG
2. Размер изображений: 800x800px для превью, 1600x1600px для полного размера
3. Имя файла: `product_id.jpg`
4. Максимальный размер файла - 2MB
5. Все изображения должны быть оптимизированы

## Формат products.json

```json
{
  "product_id": {
    "name": "Название товара",
    "slug": "nazvanie-tovara",
    "description": "Описание товара",
    "price": 1000.00,
    "currency": "RUB",
    "category_id": "category_id",
    "manufacturer": "Производитель",
    "sku": "SKU123",
    "stock": 10,
    "active": true,
    "images": [
      "product_id_1.jpg",
      "product_id_2.jpg"
    ],
    "attributes": {
      "color": "Красный",
      "size": "L",
      "weight": "1.5"
    }
  }
}
```

## Формат categories.json

```json
{
  "category_id": {
    "name": "Название категории",
    "slug": "nazvanie-kategorii",
    "description": "Описание категории",
    "parent_id": null,
    "image": "category_id.jpg",
    "active": true
  }
}
```

## Интеграция с шаблонами

1. Изображения доступны через URL: `/static/shop/images/products/product_id.jpg`
2. Метаданные доступны через API: `/api/shop/products` и `/api/shop/categories`
3. Для отображения в шаблонах используйте макросы из `templates/shop/macros.html`

## Обновление

1. Добавьте новые изображения в `images/`
2. Обновите JSON файлы
3. Запустите скрипт синхронизации: `python scripts/sync_shop.py`
4. Проверьте отображение на сайте 