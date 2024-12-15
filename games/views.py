from django.shortcuts import render
from .models import Game

def home(request):
    return render(request, 'games/home.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

# Create your views here.
