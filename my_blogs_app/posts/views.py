from django.shortcuts import render, redirect
from posts.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Author, BlogPost, Comment



def home(request):
    return render(request, "home.html")

def posts(request):
    return render(request, "posts.html", {"posts": BlogPost.objects.all()})

@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        author, _ = Author.objects.get_or_create(
            user=request.user,
            defaults={"name": request.user.username},
        )
        BlogPost.objects.create(
            author=author,
            title=form.cleaned_data["title"],
            content=form.cleaned_data["content"],
        )
        return redirect("posts")
    return render(request, "create_post.html", {"form": form})

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment.objects.create(post=post, user=request.user, content=form.cleaned_data["content"])
    return redirect("post_details", post_id)

def post_details(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = post.comments.all()
    return render(request, "post_details.html", {"post": post, "comments": comments})