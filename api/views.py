# api/views.py
from rest_framework import viewsets, permissions
from .permissions import IsAdminUserOrReadOnly
from post.serializers import PostSerializer, CommentSerializer
from post.models import Post, Comment

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]
