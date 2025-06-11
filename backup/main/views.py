from django.shortcuts import render

# Create your views here.


def index(request):
    """Главная страница сайта"""
    return render(request, "main/index.html")
