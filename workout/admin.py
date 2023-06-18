from django.contrib import admin

# Register your models here.
from .models import Workout, Category, Exercise

admin.site.register(Workout)
admin.site.register(Category)
admin.site.register(Exercise)