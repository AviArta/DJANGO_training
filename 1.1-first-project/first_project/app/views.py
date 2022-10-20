import datetime
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': '/',
        'Показать текущее время': '/current_time/',
        'Показать содержимое рабочей директории': '/workdir/'
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = None
    msg = f'Текущее время: {datetime.datetime.now().time()}'
    return HttpResponse(msg)


def workdir_view(request):
    result = listdir()
    return HttpResponse(result)
    raise NotImplemented
