from django.contrib import admin
from .models import Player, Game, GoalsScored, Profile, Team

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(GoalsScored)
class GoalsScoredAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
