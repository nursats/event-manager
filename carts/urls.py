from django.contrib import admin
from django.urls import path
from carts import views


app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:event_slug>/',views.cart_add, name='cart_add'),
    path('cart_change/<slug:event_slug>/',views.cart_change, name='cart_change'),
    path('cart_remove/<slug:event_slug>/', views.cart_remove, name='cart_remove'),
    
]