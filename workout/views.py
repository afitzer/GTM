from .models import Workout
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout/index.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.all()