#UTLISATEUR
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Utilisateur

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)



##
#  Fonction qui renvoie les données concernant l'utilisateur

def voirProfil(request):
	user = get_object_or_404(Utilisateur,first_name = nom) # récupération de l'objet user
	data =  {
	    'username': user.username,
	    'nom': user.nom,
	    'prenom': user.prenom,
	    'email': user.email,
	    'dateDeNaissance': user.dateDeNaissance,
	    'avatar': user.avatar,
	    'qualite': user.qualite,
	    'niveauEtude': user.niveauEtude,
	    'experience': user.experience,
 	    'description': user.description,
	} # création du ficier Json

	return JsonResponse(data)


##
#  Fonction pour se connecter

def login(request):
	user = authenticate(username=nomDeCompte, password=motDePasse)

	return HttpResponse()

##
#  S'enregistrer

def register(request)
	utilisateur.set_password(motDePasse)
	utilisateur.save()
	return HttpResponse("Profil de %s cree" % nomDeCompte)

##
#  Fonction pour consulter un profil

def consulterSonProfil(request):
	user=get_object_or_404(Utilisateur,username = nomDeCompte)
	return HttpResponse('Here is your profil %s' % (user.username)\
		+ '\n nom '+ user.last_name\
		+ '\n prenom '+ user.first_name\
		+ '\n email '+ user.email\
		+ '\n date de naissance ' + user.dateDeNaissance\
		#+ " derniere connexion "+ user.last_login\
		+ '\n localisation '+ user.localisation\
		+ '\n avatar '+ user.avatar\
		+ '\n qualite ' + user.qualite\
		+ '\n description '+ user.description)


##
#  Fonction pour éditer son profil

def editerSonProfil(request):
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
	if avatar != 'null' :
		user.avatar=avatar
	if qualite != 'null' :
		user.qualite=qualite
	if description != 'null' :
		user.description=description
	user.save()
	return HttpResponse('profil de %s edite' % user.username)

##
#   Changer de mot de passe

def changerMdp(request):
	user=get_object_or_404(Utilisateur,username = login)
	user.set_password(nouveauMotDePasse)
	user.save()
	return HttpResponse('mot de passe de %s modifie' % user.username)

##
#  

def index(request):
    return HttpResponse('You are in utilisateur')
