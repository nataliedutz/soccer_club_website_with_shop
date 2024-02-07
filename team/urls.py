from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    TeamPageView,
    PlayerPageView,
    TestPageView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("about/", AboutPageView.as_view(), name="about_page"),
    path("players/", TeamPageView.as_view(), name="players_page"),
    path("players/<int:player_id>/", PlayerPageView.as_view(), name="player_data"),
]

