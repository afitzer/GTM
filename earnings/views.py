from django.shortcuts import render
from .models import Trip, Flight, Hotel, Event
from django.views.generic import ListView
from django.views.generic.edit import CreateView

class TripListView(ListView):
    model = Trip
    template_name = 'earnings/index.html'

class TripCreateView(CreateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date', 'flights', 'hotels', 'events', 'shared']
    template_name = 'earnings/trip_form.html'
    success_url = '/trips/'

class FlightListView(ListView):
    model = Flight
    template_name = 'earnings/flights.html'

class FlightCreateView(CreateView):
    model = Flight
    fields = ['name', 'origin', 'destination', 'start_date', 'end_date', 'cost', 'airline', 'shared']
    template_name = 'earnings/flight_form.html'
    success_url = '/flights/'

class HotelListView(ListView):
    model = Hotel
    template_name = 'earnings/hotels.html'

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'hotel_chain', 'city', 'state', 'start_date', 'end_date', 'cost', 'shared']
    template_name = 'earnings/hotel_form.html'
    success_url = '/hotels/'

class EventListView(ListView):
    model = Event
    template_name = 'earnings/events.html'

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'city', 'state', 'start_date', 'end_date', 'cost', 'website', 'shared']
    template_name = 'earnings/event_form.html'
    success_url = '/events/'