from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm


# Create your views here.
def sign_in(request: HttpRequest):
    method = request.method
    if method == "GET":
        if request.user.is_authenticated:
            return redirect("posts")
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi {username.title()}, welcom back!")
                return redirect("posts")

        messages.error(request, f"Invalid usernam or password")
        return render(request, "users/login.html", {"form": form})


def sign_out(request: HttpRequest):
    logout(request)
    messages.success(request, f"You have been logged out.")
    return redirect("login")
