from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),  # Подключаем URLs из приложения main
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # Для работы с медиа-файлами
