from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
    events = Event.objects.all().order_by('start_time')
    context = {
        'title':'Home - Главная',
        'content': 'event manager',
        'events': events
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