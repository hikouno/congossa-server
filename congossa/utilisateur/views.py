#UTLISATEUR
from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import get_object_or_404

from .models import Utilisateur

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

def voirProfil(request, nom):
    return HttpResponse("You want to voir profil %s." % nom)
def login(request):
    return HttpResponse("You are in utilisateur")
def register(request):
    return HttpResponse("You are in utilisateur")
def index(request):
    return HttpResponse("You are in utilisateur")