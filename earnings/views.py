from .models import Trip, Flight, Hotel, Event
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
import subprocess

def execute_notebook():
    notebook_path = r"C:\Users\alexp\Documents\GTM\notebooks\Charts.ipynb"
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook_path])

class TripListView(ListView):
    model = Trip
    template_name = 'earnings/index.html'

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

class FlightCreateView(CreateView):
    model = Flight
    fields = ['name', 'origin', 'destination', 'start_date', 'end_date', 'cost', 'airline', 'shared']
    template_name = 'earnings/flight_form.html'
    success_url = reverse_lazy('earnings:flights')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_notebook()  # Execute the notebook after form submission
        return response

class HotelListView(ListView):
    model = Hotel
    template_name = 'earnings/hotels.html'

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'hotel_chain', 'city', 'state', 'start_date', 'end_date', 'cost', 'shared']
    template_name = 'earnings/hotel_form.html'
    success_url = reverse_lazy('earnings:hotels')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_notebook()  # Execute the notebook after form submission
        return response

class EventListView(ListView):
    model = Event
    template_name = 'earnings/events.html'

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'city', 'state', 'start_date', 'end_date', 'cost', 'website', 'shared']
    template_name = 'earnings/event_form.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_notebook()  # Execute the notebook after form submission
        return response

class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'city', 'state', 'start_date', 'end_date', 'cost', 'website', 'shared']
    template_name = 'earnings/event_form.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_notebook()  # Execute the notebook after form submission
        return response

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'earnings/event_delete.html'
    success_url = reverse_lazy('earnings:events')

    def form_valid(self, form):
        response = super().form_valid(form)
        execute_notebook()  # Execute the notebook after form submission
        return response

# display gapminder html
def gapminder(request):
    return render(request, 'earnings/gapminder_2007.html')

def chart(request):
    return render(request, 'earnings/chart.html')