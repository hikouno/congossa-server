#COMPOSANT OFFRE
from django.shortcuts import render
from .models import Competence
from .models import NiveauEtude
from .models import Qualite
# Create your views here.
##########################
def CreateCompetence(contenue):
	competence, competenceCree = Competence.objects.get_or_create(contenu=contenue)
	return competence
#	return HttpResponse("Competence %s cree" % contenu)
##########################
def CreateNiveauEtude(duree,domaine):
	niveauEtude=NiveauEtude.objects.get_or_create(duree = duree,domaine=domaine)
	return niveauEtude
	#return HttpResponse("Niveau d'etude  %s %s cree" % duree, domaine)
##########################
def CreateMetier(contenu):
	metier=Metier.Create(contenu)
	metier.save()
	return metier
#	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateQualite(contenue):
	qualite, qualiteCree=Qualite.objects.get_or_create(contenu=contenue)
	return qualite
#	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateExperience(metier,dateDebut,dateFin):
	experience=Experience.objects.get_or_create(metier=metier,dateDebut=dateDebut,dateFin=dateFin)
	return experience
#	return HttpResponse("experience %s du %s au %s cree" % metier.intitule, dateDebut, dateFin)
##########################
def CreateFormation(intitule, duree):
	formation = Formation.objects.get_or_create(intitule=intitule, duree=duree)
	return formation
	
