from django.shortcuts import render
from django.http import HttpResponse


#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)
def inscription(request, nom):
    return HttpResponse("You want to register as %s." % nom)

def desincription(request, nom):
    return HttpResponse("You want to deregister as %s." % nom)

def rechercher(request, nom):
    return HttpResponse("You want to look at %s." % nom)
	
def index(request):
    return HttpResponse("You are in offre")