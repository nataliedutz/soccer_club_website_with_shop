from django.db import models



class Player(models.Model):
    """The Player model"""
    name = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     verbose_name = "Player"

class Game(models.Model):
    """The Game Model"""
    game_date = models.DateField(max_length=10, unique=True, default='1900-01-01')
    opponent = models.CharField(max_length=255)
    score = models.CharField(max_length=10)

    def __str__(self):
        return f"Game against {self.opponent}"


class GoalsScored(models.Model):
    """The Goals Scored Model"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, to_field='game_date')
    minute = models.PositiveBigIntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, to_field='name', related_name='goals_scored')

    def __str__(self):
        return f"Goal made by {self.player.name} at {self.game.game_date}"


class Profile(models.Model):
    """The Profile Model"""
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='profile')
    height = models.FloatField()
    weight = models.FloatField()
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile of {self.player}"

class Team(models.Model):
    "The Team Model"
    team_name = models.CharField(max_length = 255)
    town = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)

    def __str__(self):
        return self.team_name
