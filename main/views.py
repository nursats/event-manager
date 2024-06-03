from django.http import HttpResponse
from django.shortcuts import render

from events.models import Categories


def index(request):


    context = {
        'title': 'Home - Главная',
    }

    return render(request, 'main/index.html', context)

