#OFFRE
import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import get_object_or_404

from .models import Offre, Demande, Experience

#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

@csrf_exempt
def ajoutOffre(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return JsonResponse({'test': "oui", 'username' : request.user.username, 'pass' : request.user.password})
    else:
        # Do something for anonymous users.
        return JsonResponse({'test': "non"})
    data =  {'test': request.body.decode('utf-8')} # création du ficier Json
    #o = Offre(metier=request.POST.)
    return JsonResponse(data)

@csrf_exempt
def ajoutDemande(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.user.is_authenticated:

        demande=Demande.objects.create(categorie=body['categorie'],
            typeContrat=body['typeOfJob'],
            dateDebut=body['dateDebut'],
            dateFin=body['dateFin'],
            city=body['city'],
            description=body['shortDescription'])
        #Experiences
        for i in range(len(body['experiences'])):
            exp = Experience.objects.create(
                metier=body['experiences'][i]['experience'],
                dateDebut=body['experiences'][i]['dateDebut'],
                dateFin=body['experiences'][i]['dateFin'])
            demande.experiencePossede.add(exp)
        #Formations
        #for i in range(len(body['formations'])):
            #form = Formation.objects.create(#TODO)
            #demande.formations.add(form)
        #Qualities
        #for i in range(len(body['tableQualities'])):
            #qual = Qualite.objects.create(#TODO)
            #demande.qualitePossede.add(qual)
        #Competences
        #for i in range(len(body['tableSkills'])):
            #comp = Competence.objects.create(#TODO)
            #demande.competencePossede.add(comp)
        #User
        demande.demandeur = request.user

        demande.save()

        return JsonResponse({'success': "OK"})
    else :
        return JsonResponse({'success': "KO"})


	# renvoie la description de la premiere annonce dont la String metier est egale a la string $nom
def voirAnnonce(request, nom):
	return HttpResponse("Une annonce pour vous:  %s." % (get_object_or_404(Offre,metier = nom).description+" propose par "+ get_object_or_404(Offre,metier = nom).recruteur.prenom))

###########################################
# Fonctions pour l'affichage des demandes #
###########################################
def getOffre(id_demande):
    offre = Demande.objects.get(id=id_demande)

    return offre

def getTypeEmploi(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    typeEmploi = offre.typeContrat

    return JsonResponse({'typeEmploi' : typeEmploi})

def getTitre(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    titre = offre.titre

    return JsonResponse({'titre' : titre})

def getQualite(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    qualite = "test" ########## A MODIFIER

    return JsonResponse({'qualite' : qualite})

def getEcole(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    ecole = "test2" ########### A MODIFIER

    return JsonResponse({'ecole' : ecole})

def getEcoleDescription(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    description = "test3" ############ A MODIFIER

    return JsonResponse({'description' : description})

def getExperiences(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    experiences = "test4" ################ A MODIFIER

    return JsonResponse({'experiences' : experiences})

def getCompetences(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    offre = getOffre(id_demande)
    competences = "test5" ########## A MODIFIER

    return JsonResponse({'competences' : competences})

def index(request):
    return HttpResponse("You are in offre")
