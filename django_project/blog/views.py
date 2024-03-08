from django.shortcuts import render
from django.http import HttpRequest
from .models import Post


# Create your views here.
def home(request: HttpRequest):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(requset: HttpRequest):
    return render(requset, "blog/about.html")
