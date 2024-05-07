from django.contrib import admin
from django.urls import path
from events import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('contacts/',views.contacts,name='contacts'),
    path('<slug:event_slug>/',views.about, name='about'),
    
]