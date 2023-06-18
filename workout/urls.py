from django.urls import path
from workout.views import WorkoutListView, WorkoutCreateView

app_name = "workout"

urlpatterns = [
    path('', WorkoutListView.as_view(), name='index'),
    path('create/', WorkoutCreateView.as_view(), name='workout_create'),
]