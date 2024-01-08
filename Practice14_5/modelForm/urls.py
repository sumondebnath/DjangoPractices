from django.urls import path
from modelForm.views import allForm

urlpatterns = [
    path("", allForm, name="allForm"),
]