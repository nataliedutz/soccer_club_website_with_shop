# posts/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, add_comment

urlpatterns = [
    path("blog/", PostListView.as_view(), name="post_list"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("blog/<int:pk>/comment/", add_comment, name="add_comment"),
]
