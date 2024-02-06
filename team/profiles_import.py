import os
import sys
import django

# Add the path to the directory containing your Django project to the Python path
django_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(django_project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

django.setup()

from team.models import Profile, Player

profiles_data = [
    {"name": "Lisa", "height": 170, "weight": 60, "nationality": "German"},
    {"name": "Alexandra", "height": 165, "weight": 55, "nationality": "German"},
    {"name": "Jessica", "height": 175, "weight": 65, "nationality": "German"},
    {"name": "Lilly", "height": 160, "weight": 50, "nationality": "German"},
    {"name": "Nicole", "height": 172, "weight": 58, "nationality": "Belgian"},
    {"name": "Jennifer", "height": 168, "weight": 62, "nationality": "Danish"},
    {"name": "Sophia", "height": 160, "weight": 55, "nationality": "German"},
    {"name": "Emma", "height": 167, "weight": 59, "nationality": "German"},
    {"name": "Olivia", "height": 175, "weight": 63, "nationality": "German"},
    {"name": "Ava", "height": 162, "weight": 54, "nationality": "Turkish"},
    {"name": "Isabella", "height": 170, "weight": 61, "nationality": "Swedish"},
    {"name": "Mia", "height": 166, "weight": 57, "nationality": "German"},
]

def import_profiles():
    for profile_data in profiles_data:
        player_name = profile_data.pop('name')
        player = Player.objects.get(name=player_name)
        Profile.objects.create(player=player, **profile_data)        


import_profiles()
