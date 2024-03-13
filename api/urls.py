# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet #,CustomLogoutView, LoginAPIView, LogoutAPIView
#from .views import custom_logout

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
   # path('login/', LoginAPIView.as_view(), name='api-login'),
    #path('api-authlogout/',  CustomLogoutView.as_view(), name='api-logout'),
]
