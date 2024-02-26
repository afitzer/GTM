from django.urls import path
from whiskey.views import index, rate_whiskey

app_name = "whiskey"

urlpatterns = [
    path("", index, name="index"),
    # path("<int:whiskey_id>/rate/", rate_whiskey, name="rate_whiskey"),
    # add more paths here as needed
]
