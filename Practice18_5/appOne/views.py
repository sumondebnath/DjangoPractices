from django.shortcuts import render, redirect
from appOne.forms import userForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = userForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Sign Up Successful.")
                return redirect("log_in")
        else:
            form = userForm()
        return render(request, "register.html", {"forms":form, "type":"Sign In"})
    else:
        return redirect("profile")


def logIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                name = form.cleaned_data["username"]
                passwrd = form.cleaned_data["password"]
                user = authenticate(username=name, password=passwrd)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect("profile")
                else:
                    messages.warning(request, "Logged In Failed")
                    return redirect("log_in")
        else:
            form = AuthenticationForm()
        return render(request, "register.html", {"forms":form, "type":"Log In"})
    else :
        return redirect("profile")
    
# @login_required
def Profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("log_in")

def logOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect("home")
    else:
        return redirect("log_in")

def ChangePasswordUsingOld(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Updated Successfully Using Old Password.")
                return redirect("profile")
        else:
            form = PasswordChangeForm(request.user)
        return render(request, "changePassword.html", {"forms":form})
    else:
        return redirect("log_in")

def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Updated Successfully.")
                return redirect("profile")
        else:
            form = SetPasswordForm(request.user)
        return render(request, "changePassword.html", {"forms":form})
    else:
        return redirect("log_in")