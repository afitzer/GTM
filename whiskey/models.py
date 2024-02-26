from django.db import models

class Whiskey(models.Model):
    name = models.CharField(max_length=200)
    distillery = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.whiskey.name} - {self.rating}"
