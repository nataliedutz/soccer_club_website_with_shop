import os
import sys
import django

# Add the path to the directory containing your Django project to the Python path
django_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(django_project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

django.setup()


from team.models import Player, Game, GoalsScored


players = [
    {"name": "Lisa", "age": 25, "position": "goalkeeper"},
    {"name": "Alexandra", "age": 26, "position": "forward"},
    {"name": "Jessica", "age": 24, "position": "middle"},
    {"name": "Lilly", "age": 21, "position": "defense"},
    {"name": "Nicole", "age": 26, "position": "goalkeeper"},
    {"name": "Jennifer", "age": 27, "position": "striker"},
    {"name": "Sophia", "age": 23, "position": "midfielder"},
    {"name": "Emma", "age": 25, "position": "forward"},
    {"name": "Olivia", "age": 22, "position": "defender"},
    {"name": "Ava", "age": 24, "position": "goalkeeper"},
    {"name": "Isabella", "age": 26, "position": "striker"},
    {"name": "Mia", "age": 23, "position": "midfielder"},
]

games_data = [
    {"game_date": "2023-01-02", "opponent": "1. FC Köln", "score": "3-1"},
    {"game_date": "2023-01-05", "opponent": "1. FC Nürnnberg", "score": "2-0"},
    {"game_date": "2023-01-06", "opponent": "1899 Hoffenheim", "score": "3-1"},
    {"game_date": "2023-01-07", "opponent": "Bayer Leverkusen", "score": "1-1"},
    {"game_date": "2023-01-08", "opponent": "Bayern München", "score": "1-1"},
    {"game_date": "2023-01-09", "opponent": "Eintracht Frankfurt", "score": "0-0"},
    {"game_date": "2023-01-10", "opponent": "MSV Duisburg", "score": "0-1"},
    {"game_date": "2023-01-11", "opponent": "RB Leipzig", "score": "0-2"},
    {"game_date": "2023-01-12", "opponent": "SC Freiburg", "score": "0-1"},
    {"game_date": "2023-10-01", "opponent": "Werder Bremen", "score": "1-0"},
    {"game_date": "2023-11-01", "opponent": "Vfl Wolfsburg", "score": "1-0"},
]

goals_data = [
    {"game_date": "2023-01-02", "minute": 15, "player_name": "Jennifer"},
    {"game_date": "2023-01-02", "minute": 30, "player_name": "Jennifer"},
    {"game_date": "2023-01-02", "minute": 15, "player_name": "Lisa"},
    {"game_date": "2023-01-05", "minute": 40, "player_name": "Isabella"},
    {"game_date": "2023-01-05", "minute": 55, "player_name": "Mia"},
    {"game_date": "2023-01-06", "minute": 10, "player_name": "Isabella"},
    {"game_date": "2023-01-06", "minute": 10, "player_name": "Jennifer"},
    {"game_date": "2023-01-06", "minute": 10, "player_name": "Isabella"},
    {"game_date": "2023-01-07", "minute": 25, "player_name": "Nicole"},
    {"game_date": "2023-01-08", "minute": 50, "player_name": "Jennifer"},
    {"game_date": "2023-10-01", "minute": 55, "player_name": "Isabella"},
    {"game_date": "2023-11-01", "minute": 70, "player_name": "Mia"},
]



def import_players():
    for player_data in players:
        Player.objects.create(**player_data)

def import_games():
    for game_data in games_data:
        Game.objects.create(**game_data)

def import_goals():
    for goal_data in goals_data:
        player_name = goal_data.pop('player_name')
        player = Player.objects.get(name=player_name)
        game_date = goal_data.pop('game_date')
        game = Game.objects.get(game_date=game_date)
        GoalsScored.objects.create(player=player, game=game, **goal_data)


if __name__ == '__main__':
    import_players()
    import_games()
    import_goals()
