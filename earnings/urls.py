from django.urls import path
from earnings.views import TripListView, FlightListView, EventListView, HotelListView, TripCreateView, FlightCreateView, HotelCreateView, EventCreateView, TripDetailView

app_name = "earnings"

urlpatterns = [
    path('', TripListView.as_view(), name='index'),
    path('flights/', FlightListView.as_view(), name='flights'),
    path('hotels/', HotelListView.as_view(), name='hotels'),
    path('events/', EventListView.as_view(), name='events'),
    path('trips/create/', TripCreateView.as_view(), name='trip_create'),
    path('flights/create/', FlightCreateView.as_view(), name='flight_create'),
    path('hotels/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
]