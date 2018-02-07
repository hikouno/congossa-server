#UTLISATEUR
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
#from django.shortcuts import get_object_or_404

from .models import Utilisateur

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

def voirProfil(request, nom):
    return HttpResponse("You want to voir profil %s." % nomDeCompte)
#######################################################
def login(request,nomDeCompte,motDePasse):
	user=authenticate(username=nomDeCompte, password=motDePasse)
	return HttpResponse("Hello %s" % user.username)
#######################################################
def register(request\
	, nomDeCompte\
	, motDePasse\
	, nom\
	, prenom\
	, email\
	, dateDeNaissance\
	, localisation\
	, competencePossede\
	, formationPossede\
	, diplomePossede\
	, description):
	utilisateur=Utilisateur.create(nomDeCompte\
		, motDePasse\
		, nom\
		, prenom\
		, email\
		, dateDeNaissance\
		, localisation\
		, competencePossede\
		, formationPossede\
		, diplomePossede\
		, description)
	utilisateur.set_password(motDePasse)
	utilisateur.save()
	return HttpResponse("Profil de %s cree" % nomDeCompte)
def index(request):
    return HttpResponse("You are in utilisateur")