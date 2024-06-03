from django.shortcuts import render,get_list_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Event, Categories

def indexx(request):
    events = Event.objects.all().order_by('start_time')
    paginator = Paginator(events, 5)
    current_page = paginator.page(1)
    context = {
        'title':'Home - Главная',
        'content': 'event manager',
        'events': events,
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
def catalog(request, category_slug):
    page = request.GET.get('page',1)
    order_by = request.GET.get('order_by',None)



    if category_slug == "all":
        events = Event.objects.all().order_by('start_time')
    else:
        events = get_list_or_404(Event.objects.filter(category__slug=category_slug))


    if order_by and order_by != 'default':
        events = events.order_by(order_by)
    
    paginator = Paginator(events,3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "events": current_page,
        "slug_url":category_slug,
    }
    return render(request, "events/index.html", context)
