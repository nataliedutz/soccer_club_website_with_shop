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
#from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth import logout as django_logout
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST 
from django.urls import reverse_lazy


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]
    authentication_classes = [SessionAuthentication]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]
    authentication_classes = [SessionAuthentication]

# class CustomLogoutView(BaseLogoutView):
#     next_page = reverse_lazy('api/')  

#     @method_decorator(require_POST)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
# class LoginAPIView(ObtainAuthToken):
#     """
#     API endpoint for user login.
#     """
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'username': user.username})


# class LogoutAPIView(APIView):
#     """
#     API endpoint for user logout.
#     """
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         # Delete the user's token to force logout
#         request.user.auth_token.delete()
#         django_logout(request)
#         return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
