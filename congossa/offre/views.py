from django.shortcuts import render
from django.http import HttpResponse


#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)
def ajoutOffre(request, nom):
    return HttpResponse("You want to ajouter Offre as %s." % nom)

def ajoutDemande(request, nom):
    return HttpResponse("You want to ajouter demande as %s." % nom)

def voirMatch(request, nom):
    return HttpResponse("You want voir vos match as %s." % nom)
	
def index(request):
    return HttpResponse("You are in offre")