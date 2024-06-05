from django.http import HttpResponse
from django.shortcuts import render

from events.models import Categories


def index(request):


    context = {
        'title': 'Home - Главная',
    }
    if request.user.is_authenticated:
        context['username'] = request.user.username

    return render(request, 'main/index.html', context)

