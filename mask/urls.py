from django.urls import path
from .views import *



urlpatterns = [
    path("mask/",mask, name="covid"),
]
