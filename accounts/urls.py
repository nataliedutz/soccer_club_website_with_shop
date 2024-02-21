from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Use Django's LoginView
    path('logout/', views.CustomLogoutView.as_view(), name='logout'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
   # path('redirect-to-home/', views.redirect_to_home, name='redirect_to_home'),
]
