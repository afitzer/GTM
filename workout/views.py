from .models import Workout, Exercise
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from itertools import groupby
from operator import attrgetter

# Create your views here.

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout/index.html'
    context_object_name = 'workouts_by_date'

    def get_queryset(self):
        workouts = Workout.objects.all()
        workouts_by_date = {date: list(workouts) for date, workouts in groupby(workouts, key=attrgetter('date'))}
        return workouts_by_date
    
class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['exercise', 'date', 'sets', 'reps', 'weight']
    success_url = reverse_lazy('workout:index')
    template_name = 'workout/workout_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.all()
        return context