from django.urls import path
from workout.views import (
    WorkoutListView,
    WorkoutCreateView,
    ExerciseListView,
    Journal,
)

app_name = "workout"

urlpatterns = [
    path("", WorkoutListView.as_view(), name="index"),
    path("create/", WorkoutCreateView.as_view(), name="workout_create"),
    path("exercises/", ExerciseListView.as_view(), name="exercises"),
    path("journal/", Journal, name="journal"),
]