from django.urls import path
from appOne.views import signUp, logIn, Profile, logOut, ChangePasswordUsingOld, ChangePassword

urlpatterns = [
    path("signup/", signUp, name="sign_up"),
    path("login/", logIn, name="log_in"),
    path("profile/", Profile, name="profile"),
    path("logout/", logOut, name="log_out"),
    path("change/old/password/", ChangePasswordUsingOld, name="old_password"),
    path("change/password/", ChangePassword, name="change_password"),
]