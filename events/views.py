from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Event, Categories
from events.utils import q_search

def about(request,event_slug):
    event = Event.objects.get(slug=event_slug)

    context = {
        "event": event,
        "title": event.name,
             
    }

    return render(request, "events/about.html", context)


def catalog(request, category_slug=None):
    page = request.GET.get('page',1)
    order_by = request.GET.get('order_by',None)
    query = request.GET.get('q',None)




    if category_slug == "all":
        events = Event.objects.all().order_by('start_time')
    elif query:
        events = q_search(query)
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
    return render(request, "events/catalog.html", context)
