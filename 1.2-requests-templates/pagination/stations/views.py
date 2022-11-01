from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

import pagination


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations_(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
    #     'bus_stations': ...,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)

def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        page_number = request.GET.get('page')
        reader = csv.DictReader(csvfile)
        CONTENT = [row for row in reader]
        bus_stations_list = []

    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': bus_stations_list,
        'page': page,
    }

    return render(request, 'stations/index.html', context)

#

# context = {
#                 'id': phone['id'],
#                 'name': phone['name'],
#                 'image': phone['image'],
#                 'price': phone['price'], # не требуется.
#                 'release_date': phone['release_date'],
#                 'lte_exists': phone['lte_exists']