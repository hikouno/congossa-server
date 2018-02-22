#UTLISATEUR
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Utilisateur
from .models import Competence
from .models import NiveauEtude
from .models import Qualite
from composantProfil.views import CreateNiveauEtude
from composantProfil.views import CreateQualite
#from composantProfil.views import EditQualite
from django.http import JsonResponse

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

def login_user(request, nomDeCompte, motDePasse):
    user = authenticate(username=nomDeCompte, password=motDePasse)
    
    if user is not None :
        login(request, user)
        return JsonResponse({'success' : True})
    else:
        logout(request)
        return JsonResponse({'success' : False})
    

def logout_user(request):
    logout(request)
    
    return JsonResponse({'success' : True})

@csrf_exempt
def changerPrenom(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	newPrenom = body['newPrenom']
	user=get_object_or_404(Utilisateur,username=login)
	user.first_name=newPrenom
	user.save()
	return HttpResponse()

@csrf_exempt
def changerNom(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	newNom = body['newNom']
	user=get_object_or_404(Utilisateur,username=login)
	user.last_name=newNom
	user.save()
	return HttpResponse()

@csrf_exempt
def changerSexe(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	newSexe = body['newSexe']
	user=get_object_or_404(Utilisateur,username=login)
	user.sexe=newSexe
	user.save()
	return HttpResponse()

@csrf_exempt
def changerMail(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	newEmail = body['newEmail']
	user=get_object_or_404(Utilisateur,username=login)
	user.email=newEmail
	user.save()
	return HttpResponse()

@csrf_exempt
def changerDateDeNaissance(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	DateDeNaissance = body['newDateDeNaisance']
	user=get_object_or_404(Utilisateur,username=login)
	user.dateDeNaissance=DateDeNaissance
	user.save()
	return HttpResponse()

@csrf_exempt
def changeTelephone(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	Telephone = body['newTelephone']
	user=get_object_or_404(Utilisateur,username=login)
	user.telephone=Telephone
	user.save()
	return HttpResponse()

@csrf_exempt
def changeDescription(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	Description = body['newDescription']
	user=get_object_or_404(Utilisateur,username=login)
	user.description=Description
	user.save()
	return HttpResponse()

@csrf_exempt
def createDiplome(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	login = body['login']
	domaineDiplome = body['newDescription']
	dureeDiplome = body['newDureeDiplome']
	user=get_object_or_404(Utilisateur,username=login)
	diplome=NiveauEtude.create()
	user.niveauEtude.add
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

def ajouterCompetence(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.competence.add(CreateCompetence(request.POST.contenuCompetence))
	user.save()
########
def editeCompetence(request):
	competence = get_objet_or_404(Competence, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.competence.exclude(competence=competence)
	user.add(CreateCompetence(request.POST.contenu))
	user.save()
########
def removeCompetence(request):
	niveauEtude = get_objet_or_404(Competence, id=request.POST.id)
	user.competence.exclude(competence=competence)
	user.save()
###########################################
def ajouterNiveauEtude(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.add(CreateNiveauEtude(request.POST.duree,request.POST.domaine))
	user.save()
########
def editeNiveauEtude(request):
	niveauEtude= get_objet_or_404(NiveauEtude, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.niveauEtude.exclude(niveauEtude=niveauEtude)
	user.add(CreateNiveauEtude(request.POST.newDuree,request.POST.newDomaine))
	user.save()
########
def removeNiveauEtude(request):
	niveauEtude = get_objet_or_404(NiveauEtude, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.niveauEtude.exclude(niveauEtude=niveauEtude)
	user.save()
###########################################
def ajouterQualite(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.qualite.add(CreateQualite(request.POST.qualiteAjoutee))
	user.save()
######
def editQualite(request):
	qualite= get_objet_or_404(Qualite, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.qualite.exclude(qualite=qualite)
	user.qualite.add(CreateQualite(request.POST.qualiteAjoutee))
	user.save()
######
def removeQualite(request):
	qualite= get_objet_or_404(Qualite, id=request.POST.id)
	user.qualite.exclude(qualite=qualite)
	user.save()
###########################################
def ajouterExperience(request):
	user=get_object_or_404(Utilisateur, username = request.POST.username)
	user.add(Experience.create(request.POST.idMetier,request.POST.dateDebut,request.POST.dateFin))
	user.save()
def editExperience(request):
	experience= get_objet_or_404(Experience, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.experience.exclude(experience=experience)
	user.experience.add(CreateQualite(request.POST.idNewMetier,request.POST.newDateDebut,request.POST.newDateFin))
	user.save()
######
def removeExperience(request):
	experience= get_objet_or_404(Experience, id=request.POST.id)
	user = get_objet_or_404(Utilisateur, username=request.POST.username)
	user.experience.exclude(experience=experience)
	user.save()
###########################################
#def editerMonProfil(request):
#	user=get_object_or_404(Utilisateur, username= request.POST.username)
#	#Competence
#	for i in range(1,request.POST.nbCompetence):
#		if request.POST.actionCompetence[i] == "add":
#			ajouterCompetence(request.POST.username,request.POST.competence[i])
#		elif request.POST.actionCompetence[i]=="edit":
#			editCompetence(request.POST.username,request.POST.idCompetence[i],request.POST.competence[i])
#		elif request.POST.actionCompetence[i]=="remove":
#			removeCompetence(request.POST.username,request.POST.idCompetence[i])
#
#	#Niveau d etude
#	for i in range(1,request.POST.nbNiveauEtude):
#		if request.POST.actionNiveauEtude[i]=="add":
#			ajouterNiveauEtude(request.POST.username,request.POST.dureeNiveauEtude[i],request.POST.domaineNiveauEtude[i])
#		elif request.POST.actionNiveauEtude[i]=="edit":
#			editNiveauEtude(request.POST.username,request.POST.idNiveauEtude[i],request.POST.dureeNiveauEtude[i],request.POST.domaineNiveauEtude[i])
#		elif request.POST.actionNiveauEtude[i]=="remove":
#			removeNiveauEtude(request.POST.username,request.POST.idNiveauEtude[i])
#	#Qualite
#	for i in range(1,request.POST.nbQualite):
#		if request.POST.actionQualite[i]=="add":
#			ajouterQualite(request.POST.username,request.POST.contenuQualite[i])
#		elif request.POST.actionQualite[i]=="edit":
#			editQualite(request.POST.username,request.POST.idQualite[i],request.POST.contenuQualite[i])
#		elif request.POST.actionQualite[i]=="remove":
#			removeQualite(request.POST.username,request.POST.idQualite[i])
def index(request):
    return HttpResponse('You are in utilisateur')
