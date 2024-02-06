from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import render
from .models import Player


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class TeamPageView(TemplateView):
    template_name = "team.html"

    def get_context_data(self):
        players = Player.objects.all()
        context = {"players": players}
        return context


class PlayerPageView(TemplateView):
    template_name = "player.html"

    def get_context_data(self, player_id):
        player = Player.objects.get(id=player_id)
        context = {"player": player}
        return context
    

class TestClass():

    textattr = "testattr"
    def __init__(self, text:str):
        self.text = text

    def get(self):
        return self.text.upper()
    
    @classmethod
    def getmethod(cls):
        return cls.textattr.upper()
    
class TestPageView(TemplateView):
    template_name = "test.html"

    def get_context_data(self):
        testobj = TestClass("instancestring")
        context = {"textlist": ["one", "two", "three"], 
                   "testobj": testobj, 
                   "emptylist": [],
                    "b": 100,
                    "names":"first, second, third",
                    "username": "george", 
                    "heading": "This is an example of 'escaping' with the characters > , > and &"}
        return context
























# from django.http import HttpResponse
# from django.urls import reverse
# from django.shortcuts import get_object_or_404
# from .models import Player
# from .data_import import players, goals_data



# def home_page_view(request):
#     url = reverse("about_page")
#     url1 = reverse("team_page")
#     url2 = reverse("player_page", args=[0])
#     url3 = reverse("scorers_page")

#     page = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <a href = "{url}">About Page</a>
#     <a href = "{url1}">Team Page</a>
#     <a href = "{url2}">Player Page</a>
#     <a href = "{url3}">Top Scorers Page</a>
#     <h1>This is the homepage of our Team</h1>
#     <p>This is the page with info about our team</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(page)


# def about_page_view(request):
#     url = reverse("home_page")
#     url1 = reverse("team_page")
#     url2 = reverse("player_page", args=[0])
#     url3 = reverse("scorers_page")


#     page = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <a href = "{url}">Home Page</a>
#     <a href = "{url1}">Team Page</a>
#     <a href = "{url2}">Player Page</a>
#     <a href = "{url3}">Top Scorers Page</a>

#     <h1>About</h1>
#     <p>Here you can find information about our team.</p>
#     <h2>Contact data</h2>
#     <p>Address line 1</p>
#     <p>Address line 2</p>
#     <p>Address line 3</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(page)


# def team_page_view(request):
#     url = reverse("home_page")
#     url1 = reverse("about_page")
#     url3 = reverse("player_page", args=[0])
#     url4 = reverse("scorers_page")
    
#     page_part1 = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <a href = "{url}">Home Page</a>
#     <a href = "{url1}">About Page</a>
#     <a href = "{url3}">Player Page</a>
#     <a href = "{url4}">Top Scorers Page</a>


#     <h1>Players of our Team</h1>
#     <p>This is the page with info about our team</p>
#     <ol>
#     """
#     index = 0
#     for player in players:
#         player_url = reverse("player_page", args=[index])
#         page_part1 += f'<li><a href ="{player_url}">' + player["name"] + "</a></li>"
#         index += 1

#     page_part2 = """
#     </ol>
#     </body>
#     </html>
#     """

#     return HttpResponse(page_part1 + page_part2)


# def player_page_view(request, player_id):
#     url = reverse("home_page")
#     url1 = reverse("about_page")
#     url2 = reverse("team_page")
#     url4 = reverse("scorers_page")

#     player = get_object_or_404(Player, id=player_id)

#     page = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Team</title>
#     </head>
#     <body>
#     <a href = "{url}">Home Page</a>
#      <a href = "{url1}">About Page</a>
#     <a href = "{url2}">Team Page</a>
#     <a href = "{url4}">Top Scorers Page</a>
#     <h1>About Player {player_id}</h1>
#     <p>Name: {players[player_id]["name"]}</p>
#     <p>Age: {players[player_id]["age"]}</p>
#     <p>Position: {players[player_id]["position"]}</p>
#     <h2>Profile:</h2>
#     <p>Height: {player.profile.height}</p>
#     <p>Weight: {player.profile.weight}</p>
#     <p>Nationality: {player.profile.nationality}</p>

#     </body>
#     </html>
#     """
#     return HttpResponse(page)

# def scorers_page_view(request):
#     url = reverse("home_page")
#     url1 = reverse("about_page")
#     url2 = reverse("team_page")
#     url3 = reverse("player_page", args=[0])


#     # Calculate the number of goals scored by each player
#     scorers = {}
#     for goal_data in goals_data:
#         player_name = goal_data["player_name"]
#         scorers[player_name] = scorers.get(player_name, 0) + 1

#     # Sort players by the number of goals scored
#     sorted_scorers = sorted(scorers.items(), key=lambda x: x[1], reverse=True)

#     page = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <title>Our Scorers</title>
#     </head>
#     <body>
#     <a href = "{url}">Home Page</a>
#     <a href = "{url1}">About Page</a>
#     <a href = "{url2}">Team Page</a>
#     <a href = "{url3}">Player Page</a>
#     <h1>Top Scorers</h1>
#     <ol>
#     """

#     for player_name, goals_scored in sorted_scorers:
#         player_url = reverse("player_page", args=[players.index(next(p for p in players if p["name"] == player_name))])
#         page += f'<li><a href="{player_url}">{player_name}</a> - Goals: {goals_scored}</li>'

#     page += """
#     </ol>
#     </body>
#     </html>
#     """

#     return HttpResponse(page)
