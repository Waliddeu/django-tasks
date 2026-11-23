from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import BlogPost, Comment



def home(request):
    return render(request, "home.html")

def posts(request):
    template = loader.get_template('posts.html')
    return HttpResponse(template.render())

@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        author = form.cleaned_data["author"]
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        return redirect("success")
    return render(request, "create_post.html", {"form": form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    comment = Comment(post=post, user=request.user)
    comment.save()