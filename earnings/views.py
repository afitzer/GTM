from .models import Trip, Flight, Hotel, Event
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
import subprocess
import sys
import os
from django.utils import timezone
import requests
from django.conf import settings
from django.http import JsonResponse

def execute_chart_update():
    chart_update_path = r"C:\Users\alexp\Documents\GTM\notebooks\chart_update.py"

    # Activate the virtual environment
    venv_path = r"C:\Users\alexp\Documents\GTM\.venv\Scripts\activate"
    activate_cmd = f"source {venv_path}" if sys.platform.startswith("linux") else f"activate {venv_path}"
    subprocess.run(activate_cmd, shell=True, check=True)

    # Execute the chart_update.py script using the python command
    subprocess.run([sys.executable, chart_update_path])

class TripListView(ListView):
    model = Trip
    template_name = 'earnings/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['upcoming_trips'] = self.get_queryset().filter(start_date__gte=today)
        context['past_trips'] = self.get_queryset().filter(start_date__lt=today)
        return context

class TripDetailView(DetailView):
    model = Trip
    template_name = 'earnings/trip_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.filter(trip=self.object)
        context['hotels'] = Hotel.objects.filter(trip=self.object)
        context['events'] = Event.objects.filter(trip=self.object)
        return context
    
class TripCreateView(CreateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date', 'flights', 'hotels', 'events', 'shared']
    success_url = reverse_lazy('earnings:index')
    template_name = 'earnings/trip_form.html'

class FlightListView(ListView):
    model = Flight
    template_name = 'earnings/flights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['upcoming_flights'] = self.get_queryset().filter(start_date__gte=today)
        context['past_flights'] = self.get_queryset().filter(start_date__lt=today)
        return context

class FlightCreateView(CreateView):
    model = Flight
    fields = ['name', 'origin', 'destination', 'start_date', 'end_date', 'cost', 'airline', 'shared']
    template_name = 'earnings/flight_form.html'
    success_url = reverse_lazy('earnings:flights')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_chart_update()
        return response

class HotelListView(ListView):
    model = Hotel
    template_name = 'earnings/hotels.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['upcoming_hotels'] = self.get_queryset().filter(start_date__gte=today)
        context['past_hotels'] = self.get_queryset().filter(start_date__lt=today)
        return context

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'hotel_chain', 'city', 'state', 'start_date', 'end_date', 'cost', 'shared']
    template_name = 'earnings/hotel_form.html'
    success_url = reverse_lazy('earnings:hotels')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_chart_update()
        return response

class EventListView(ListView):
    model = Event
    template_name = 'earnings/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['upcoming_events'] = self.get_queryset().filter(start_date__gte=today)
        context['past_events'] = self.get_queryset().filter(start_date__lt=today)
        return context

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'city', 'state', 'start_date', 'end_date', 'cost', 'website', 'shared']
    template_name = 'earnings/event_form.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_chart_update()
        return response

class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'city', 'state', 'start_date', 'end_date', 'cost', 'website', 'shared']
    template_name = 'earnings/event_form.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_chart_update()
        return response

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'earnings/event_delete.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_chart_update()
        return response

# display gapminder html
def gapminder(request):
    return render(request, 'earnings/gapminder_2007.html')

def chart(request):
    return render(request, 'earnings/chart.html')

def get_weather(request):
    api_key = settings.WEATHER_API_KEY
    api_url = settings.WEATHER_API_URL
    city_name = request.GET.get('city', 'London')  # Default city is London

    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Unable to fetch weather data.'}, status=500)