#UTLISATEUR
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Utilisateur
from .models import Competence
from .models import NiveauEtude
from .models import Qualite

from composantProfil.views import EditCompetence
from composantProfil.views import EditNiveauEtude
#from composantProfil.views import EditQualite


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

def register(request):
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
# GESTION COMPOSANT PROFIL
###########################################

def ajouterNiveauEtude(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.add(NiveauEtude.create(request.POST.duree,request.POST.domaine))
########
def removeNiveauEtude(request):
	niveauEtude = get_objet_or_404(NiveauEtude, id=request.POST.id)
	niveauEtude.delete()
########
def editeNiveauEtude(request):
	niveauEtude= get_objet_or_404(NiveauEtude, id=request.POST.id)
	EditNiveauEtude(competence,request.POST.newDuree,request.POST.newDomaine)

###########################################

def ajouterQualite(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.add(Qualite.create(request.POST.qualiteAjoutee))
######
def removeQualite(request):
	qualite= get_objet_or_404(Qualite, id=request.POST.id)
	qualite.delete()
#######
#def editeQualite(request):
#	qualite= get_objet_or_404(Qualite, id=request.POST.id)
#	EditCompetence(qualite,request.POST.newContent)

###########################################

def ajouterExperience(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.add(Experience.create(request.POST.idMetier,request.POST.dateDebut,request.POST.dateFin))
###########################################
def editerMonProfil(request):
	user=get_object_or_404(Utilisateur, username= request.POST.username)
	#Competence
	for i in range(1,request.POST.nbCompetence):
		if request.POST.actionCompetence[i] == "add":
			ajouterCompetence(request.POST.competence[i])
		elif request.POST.actionCompetence[i]=="edit":
			editCompetence(request.POST.idCompetence[i],request.POST.competence[i])
		elif request.POST.actionCompetence[i]=="remove":
			removeCompetence(request.POST.idCompetence[i])

	#Niveau d etude
	for i in range(1,request.POST.nbNiveauEtude):
		if request.POST.actionNiveauEtude[i]=="add":
			ajouterNiveauEtude(request.POST.dureeNiveauEtude[i],request.POST.domaineNiveauEtude[i])
		elif request.POST.actionNiveauEtude[i]=="edit":
			editNiveauEtude(request.POST.idNiveauEtude[i],request.POST.dureeNiveauEtude[i],request.POST.domaineNiveauEtude[i])
		elif request.POST.actionNiveauEtude[i]=="remove":
			removeNiveauEtude(request.POST.idNiveauEtude[i])
def index(request):
    return HttpResponse('You are in utilisateur')
