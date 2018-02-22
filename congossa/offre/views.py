#OFFRE
import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import get_object_or_404

from .models import Offre, Demande

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

        print(body['categorie'])
        print(body['city'])
        print(body['dateDebut'])
        print(body['dateFin'])
        print(body['experiences'])
        print(body['formations'])
        print(body['shortDescription'])
        print(body['tableQualities'])
        print(body['tableSkills'])
        print(body['typeOfJob'])

        demande=Demande.Create(categorie=body['categorie'],
            typeContrat=body['typeOfJob'],
            dateDebut=body['dateDebut'],
            dateFin=body['dateFin'],
            city=body['city'],
            description=body['shortDescription'])
        #Experiences
        #for i in range(len(body['experiences'])):
            #exp = Experience.objects.create()
            #demande.experiencePossede.add(experience)
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

def index(request):
    return HttpResponse("You are in offre")
