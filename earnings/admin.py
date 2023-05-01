from django.contrib import admin

# Register your models here.
from .models import Trip, Flight, Hotel, Event

admin.site.register(Trip)
admin.site.register(Flight)
admin.site.register(Hotel)
admin.site.register(Event)