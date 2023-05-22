from django.urls import path
from earnings.views import TripListView, TripCreateView, FlightListView, EventListView, HotelListView, FlightCreateView, HotelCreateView, EventCreateView, TripDetailView, gapminder, EventUpdateView, EventDeleteView

app_name = "earnings"

urlpatterns = [
    path('', TripListView.as_view(), name='index'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('trips/create/', TripCreateView.as_view(), name='trip_create'),
    path('flights/', FlightListView.as_view(), name='flights'),
    path('flights/create/', FlightCreateView.as_view(), name='flight_create'),
    path('hotels/', HotelListView.as_view(), name='hotels'),
    path('hotels/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('events/', EventListView.as_view(), name='events'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('gapminder/', gapminder, name='gapminder'),
]