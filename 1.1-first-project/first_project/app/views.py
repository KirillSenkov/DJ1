from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request: HttpRequest) -> HttpResponse:
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request: HttpRequest) -> HttpResponse:
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%H:%M:%S')
    msg = f'<a href={reverse("home")}>Текущее время:</a> {current_time}'
    return HttpResponse(msg)

def dirlist_column(dirlist: list):
    result = '<br>'.join(dirlist)
    return result

def workdir_view(request: HttpRequest) -> HttpResponse:
    path = os.path.dirname(__file__)
    dirlist = os.listdir(path)
    msg = f'<a href={reverse("home")}>Содержимое рабочей директории:</a><br>'\
          + dirlist_column(dirlist)
    return HttpResponse(msg)
