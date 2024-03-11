from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
def home(request: HttpRequest):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(requset: HttpRequest):
    return render(requset, "blog/about.html")


def create_post(request: HttpRequest):
    method = request.method
    if method == "GET":
        context = {"form": PostForm()}
        return render(request, "blog/post_form.html", context)
    elif method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("posts")
        else:
            messages.error(request, "Please correct the following errors:")
            return render(request, "blog/post_form.html", {"form": form})


def edit_post(request: HttpRequest, id):
    post = get_object_or_404(Post, id=id)
    method = request.method

    if method == "GET":
        context = {"form": PostForm(instance=post), "id": id}
        return render(request, "blog/post_form.html", context)
    elif method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been updated successfully.")
            return redirect("posts")
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})
