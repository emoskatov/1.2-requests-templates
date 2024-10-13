from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pprint import pprint


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
    csv = csv.DictReader(file)
    stations = list(csv)


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 13)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {

         'bus_stations': page,
         'page': page

    }
    return render(request, 'stations/index.html', context)
