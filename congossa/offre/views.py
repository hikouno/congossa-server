from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Offre, Demande

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

def ajoutOffre(request, nom):
    return HttpResponse("You want to ajouter Offre as %s." % nom)

def ajoutDemande(request, nom):
	return HttpResponse("You want to ajouter demande as %s." % nom)
	# renvoie la description de la premiere annonce dont la String metier est egale a la string $nom
def voirAnnonce(request, nom):
	return HttpResponse("Une annonce pour vous:  %s." % get_object_or_404(Offre,metier = nom).description)
	
def index(request):
    return HttpResponse("You are in offre")