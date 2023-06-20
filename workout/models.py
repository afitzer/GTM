from django.db import models

class Workout(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    date = models.DateField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.exercise.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
   
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name