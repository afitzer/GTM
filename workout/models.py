from django.db import models

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.name
    