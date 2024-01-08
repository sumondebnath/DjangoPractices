from django.urls import path
from formAPI.views import home

urlpatterns = [
    path("", home, name="home"),
]