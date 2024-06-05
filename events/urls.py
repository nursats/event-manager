from django.contrib import admin
from django.urls import path
from events import views


app_name = 'events'
urlpatterns = [
    path('search/',views.catalog, name='search'),
    path('event/<slug:event_slug>/',views.about, name='about'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    
]