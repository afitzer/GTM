from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    flights = models.ManyToManyField("Flight")
    hotels = models.ManyToManyField("Hotel")
    events = models.ManyToManyField("Event")
    shared = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_total_cost(self):
        total = 0
        for flight in self.flights.all():
            total += flight.cost
        for hotel in self.hotels.all():
            total += hotel.cost
        for event in self.events.all():
            total += event.cost
        return total
    
class Flight(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    airline = models.CharField(max_length=60)
    shared = models.BooleanField(default=False)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    hotel_chain = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    shared = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    website = models.URLField()
    shared = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.name