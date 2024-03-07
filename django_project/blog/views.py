from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

posts = [
    {
        "title": "Beautiful is better than ugly",
        "author": "John Doe",
        "content": "Beautiful is better than ugly",
        "published_at": "October 1, 2022",
    },
    {
        "title": "Explicit is better than implicit",
        "author": "Jane Doe",
        "content": "Explicit is better than implicit",
        "published_at": "October 1, 2022",
    },
]


# Create your views here.
def home(request: HttpRequest):
    context = {"posts": posts, "title": "Zen of Python"}
    return render(request, "blog/home.html", context)


def about(requset: HttpRequest):
    return render(requset, "blog/about.html")
