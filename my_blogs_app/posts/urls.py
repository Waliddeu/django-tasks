from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post_details, name='post_details'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('create_post/', views.create_post, name='create_post'),
]