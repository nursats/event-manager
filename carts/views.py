from django.shortcuts import redirect, render

from events.models import Event
from carts.models import Cart

def cart_add(request, event_slug):
    event = Event.objects.get(slug=event_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, event=event)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity+=1
                cart.save()
        else:
            Cart.objects.create(user=request.user,event=event,quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])



def cart_change(request, event_slug):
    pass


def cart_remove(request, event_slug):
    pass