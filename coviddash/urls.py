from django.urls import path
from .views import *



urlpatterns = [
    path("covid-dashboard/",covid, name="covid"),
]
