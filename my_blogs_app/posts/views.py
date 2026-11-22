from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from posts.forms import PostForm


def home(request):
    return render(request, "home.html")

def posts(request):
    template = loader.get_template('posts.html')
    return HttpResponse(template.render())

def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        author = form.cleaned_data["author"]
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        return redirect("success")
    return render(request, "create_post.html", {"form": form})