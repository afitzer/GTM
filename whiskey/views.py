from django.shortcuts import render
from .models import Whiskey, Rating

def index(request):
    whiskeys = Whiskey.objects.all()
    return render(request, "whiskey/index.html", {"whiskeys": whiskeys})


def rate_whiskey(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    if request.method == "POST":
        rating = Rating(
            whiskey=whiskey, user=request.user, rating=request.POST["rating"]
        )
        rating.save()
    return render(request, "whiskey_ratings/rate.html", {"whiskey": whiskey})
