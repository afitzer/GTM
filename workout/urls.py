from django.urls import path
from workout.views import WorkoutListView

app_name = "workout"

urlpatterns = [
    path('', WorkoutListView.as_view(), name='index'),
]