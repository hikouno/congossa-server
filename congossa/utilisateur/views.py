#UTLISATEUR
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import Utilisateur

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

def voirProfil(request, nom):
	return HttpResponse("You want to voir profil de %s" % get_object_or_404(Utilisateur,first_name = nom).username)
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
def consulterSonProfil(request,nomDeCompte):
	return HttpResponse("Her is your profil %s" % get_object_or_404(Utilisateur,username = nomDeCompte).username)
# On verra apres pour le login et mdp
def editerSonProfil(request\
	, login\
	, nom\
	, prenom\
	, email\
	, dateDeNaissance\
	, localisation\
	, competencePossede\
	, formationPossede\
	, diplomePossede\
	, description):
	# Du coup si une string est 'null' on change rien
	user=get_object_or_404(Utilisateur,username = login)
	if nom != 'null' :
		user.last_name=nom
	if prenom != 'null' :
		user.first_name=prenom
	if email != 'null' :
		user.email=email
	if dateDeNaissance != 'null' :
		user.dateDeNaissance=dateDeNaissance
	if localisation != 'null' :
		user.localisation=localisation
	if competencePossede != 'null' :
		user.competencePossede=competencePossede
	if formationPossede != 'null' :
		user.formationPossede=formationPossede
	if diplomePossede != 'null' :
		user.diplomePossede=diplomePossede
	if description != 'null' :
		user.description=description
	user.save()
	return HttpResponse("profil de %s edite" % user.username)
def index(request):
    return HttpResponse("You are in utilisateur")