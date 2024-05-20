from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Event

def index(request):
    events = Event.objects.all().order_by('start_time')
    paginator = Paginator(events, 5)
    current_page = paginator.page(1)
    context = {
        'title':'Home - Главная',
        'content': 'event manager',
        'events': current_page,
    }
    
    return render(request, 'events/index.html',context)

def about(request,event_slug):
    event = Event.objects.get(slug=event_slug)

    context = {
        "event": event,
        "title": event.name       
    }

    return render(request, "events/about.html", context)

def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request,"events/contacts.html" , context)