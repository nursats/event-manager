from django.contrib import admin
from .models import Event, Categories

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Categories)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}