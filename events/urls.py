from django.contrib import admin
from django.urls import path
from events import views


app_name = 'events'
urlpatterns = [
    path('', views.indexx, name = 'home'),
    path('contacts/',views.contacts,name='contacts'),
    path('search/',views.contacts,name='search'),
    path('event/<slug:event_slug>/',views.about, name='about'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    
]