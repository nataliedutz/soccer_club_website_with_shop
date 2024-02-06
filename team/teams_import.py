import os
import sys
import django

# Add the path to the directory containing your Django project to the Python path
django_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(django_project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

django.setup()


from team.models import Player, Game, GoalsScored, Team

teams = [
    {"team_name": "Werder Bremen", "town": "Bremen", "color": "green white"},
    {"team_name": "MSV Duisburg", "town": "Duisburg", "color": "blue white"},
    {"team_name": "Eintracht Frankfurt", "town": "Frankfurt", "color": "red white"},
    {"team_name": "SC Freiburg", "town": "Freiburg", "color": "black white"},
    {"team_name": "TSG 1899 Hoffenheim", "town": "Hoffenheim", "color": "blue white"},
    {"team_name": "1. FC Köln", "town": "Köln", "color": "red black white"},
    {"team_name": "RB Leipzig", "town": "Leipzig", "color": " white black red"},
    {"team_name": "Bayer 04 Leverkusen", "town": "Leverkusen", "color": "red yellow"},
    {"team_name": "FC Bayern München", "town": "München", "color": "red blue white"},
    {"team_name": "1. FC Nürnberg", "town": "Nürnberg", "color": "red white"},
    {"team_name": "VfL Wolfsburg", "town": "Wolfsburg", "color": "green white"},
    {"team_name": "SGS Essen-Schönebeck", "town": "Essen", "color": "purple white"},
]
