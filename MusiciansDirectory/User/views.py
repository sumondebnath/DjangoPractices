from django.shortcuts import render, redirect
from User.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
def Register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log_in")
    else:
        form = UserForm()
    return render(request, "register.html", {"form":form, "type":"Register"})


class LogIn(LoginView):
    template_name = "register.html"

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Log In"
        return context
    
    def get_success_url(self):
        return reverse_lazy("home")
    
    
class LogOut(LogoutView):
    def get_success_url(self):
        return reverse_lazy("home")