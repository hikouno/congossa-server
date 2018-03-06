#OFFRE
import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Offre, Demande, Experience, Metier, Qualite, Competence
from .serializers import DemandeSerializer, OffreSerializer



#Les fonctions a appeler les parametres sont recuperer dans urls.py (nom dans mon cas)

@csrf_exempt
def ajoutOffre(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.user.is_authenticated:

        print(body)



        metier1, metier_bool = Metier.objects.get_or_create(intitule=body['categorie'])
        offre=Offre.objects.create(titre=body['title'],
            categorie=metier1,
            typeContrat=body['typeOfJob'],
            dateDebut=body['dateDebut'],
            dateFin=body['dateFin'],
            city=body['city'],
            description=body['description'])
        #Experiences
        for i in range(len(body['experiences'])):
            metier, bool =Metier.objects.get_or_create(
                intitule=body['experiences'][i]['domaine'])
            exp = Experience.objects.create(
                titre=body['experiences'][i]['experience'],
                domaine=metier,
                duree=body['experiences'][i]['period'])
            offre.experiencesRequises.add(exp)
        #Qualities
        for i in range(len(body['tableQualities'])):
            qual, qual_bool = Qualite.objects.get_or_create(contenu=body['tableQualities'][i])
            offre.qualitesRequises.add(qual)
        #Competences
        for i in range(len(body['tableSkills'])):
            comp, comp_bool = Competence.objects.get_or_create(contenu=body['tableSkills'][i])
            offre.competencesRequises.add(comp)
        #User
        offre.recruteur = request.user

        offre.save()

        print('offre créée :')
        print(offre.qualitesRequises.all())

        return JsonResponse({'success': "OK"})
    else :

        return JsonResponse({'success': "KO"})
@csrf_exempt
def ajoutDemande(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.user.is_authenticated:

        print(body)

        metier1, metier_bool = Metier.objects.get_or_create(intitule=body['categorie'])
        demande=Demande.objects.create(categorie=metier1,
            typeContrat=body['typeOfJob'],
            dateDebut=body['dateDebut'],
            dateFin=body['dateFin'],
            city=body['city'],
            description=body['shortDescription'])
        #Experiences
        for i in range(len(body['experiences'])):
            metier, bool =Metier.objects.get_or_create(
                intitule=body['experiences'][i]['domaine'])
            exp = Experience.objects.create(
                titre=body['experiences'][i]['experience'],
                domaine=metier,
                duree=body['experiences'][i]['period'])
            demande.experiencePossede.add(exp)
        #Qualities
        for i in range(len(body['tableQualities'])):
            qual, qual_bool = Qualite.objects.get_or_create(contenu=body['tableQualities'][i])
            demande.qualitePossede.add(qual)
        #Competences
        for i in range(len(body['tableSkills'])):
            comp, comp_bool = Competence.objects.get_or_create(contenu=body['tableSkills'][i])
            demande.competencePossede.add(comp)
        #User
        demande.demandeur = request.user

        demande.save()

        return JsonResponse({'success': "OK"})
    else :
        return JsonResponse({'success': "KO"})


	# renvoie la description de la premiere annonce dont la String metier est egale a la string $nom
def voirAnnonce(request, nom):
	return HttpResponse("Une annonce pour vous:  %s." % (get_object_or_404(Offre,metier = nom).description+" propose par "+ get_object_or_404(Offre,metier = nom).recruteur.prenom))



def getDemandes(request):

    if request.user.is_authenticated:

        demandes = get_list_or_404(Demande, demandeur = request.user)
        demandes_json = DemandeSerializer(demandes, many=True)

        return JsonResponse(demandes_json.data, safe=False)
    else :
        return JsonResponse({'success': False})

def getOffres(request):

    if request.user.is_authenticated:

        offres = get_list_or_404(Offre, recruteur = request.user)
        offres_json = OffreSerializer(offres, many=True)


        return JsonResponse(offres_json.data, safe=False)
    else :
        return JsonResponse({'success': False})

###########################################
# Fonctions pour l'affichage des demandes #
###########################################
def getDemande(id_demande):
    demande = Demande.objects.get(id=id_demande)

    return demande

def getLocalisation(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    localisation = demande.localisation

    return JsonResponse({'localisation' : localisation})

def getTypeEmploi(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    typeEmploi = demande.typeContrat

    return JsonResponse({'typeEmploi' : typeEmploi})

def getTitre(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    titre = demande.titre

    return JsonResponse({'titre' : titre})

def getQualite(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    qualite = "test" ########## A MODIFIER

    return JsonResponse({'qualite' : qualite})

def getEcole(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    ecole = "test2" ########### A MODIFIER

    return JsonResponse({'ecole' : ecole})

def getEcoleDescription(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    description = "test3" ############ A MODIFIER

    return JsonResponse({'description' : description})

def getExperiences(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    experiences = "test4" ################ A MODIFIER

    return JsonResponse({'experiences' : experiences})

def getCompetences(request):
    # Récupération du fichier json
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_demande = body['id_demande']

    demande = getDemande(id_demande)
    competences = "test5" ########## A MODIFIER

    return JsonResponse({'competences' : competences})

def index(request):
    return HttpResponse("You are in offre")
