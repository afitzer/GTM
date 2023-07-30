from .models import Workout, Exercise
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from itertools import groupby
from operator import attrgetter
from django.db.models import Q
from django.shortcuts import render

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

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'workout/exercises.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Get the value of the 'q' parameter from the URL
        exercises = super().get_queryset()
        
        if query:
            # Filter the exercises based on the 'name' field using a case-insensitive search
            # exercises = exercises.filter(Q(name__icontains=query))

            # Filter the exercises based on the 'category' field using a case-insensitive search
            exercises = exercises.filter(Q(category__name__icontains=query))

        return exercises

def Journal(request):
    return render(request, 'workout/journal.html')