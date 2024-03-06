# api/views.py
from rest_framework import viewsets, permissions
from .permissions import IsAdminUserOrReadOnly
from post.serializers import PostSerializer, CommentSerializer
from post.models import Post, Comment

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout as django_logout

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

class LoginAPIView(ObtainAuthToken):
    """
    API endpoint for user login.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.get_or_create(user=user)
        return Response({'token': user.auth_token.key})


class LogoutAPIView(APIView):
    """
    API endpoint for user logout.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the user's token to force logout
        request.user.auth_token.delete()
        django_logout(request)
        return Response(status=status.HTTP_200_OK)
