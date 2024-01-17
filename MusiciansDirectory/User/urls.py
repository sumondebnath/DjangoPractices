from django.urls import path 
from User.views import Register, LogIn, LogOut

urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", LogIn.as_view(), name="log_in"),
    path("logout/", LogOut.as_view(), name="log_out"),
]