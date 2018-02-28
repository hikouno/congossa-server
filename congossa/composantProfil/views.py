#COMPOSANT OFFRE
from django.shortcuts import render
from .models import Competence
from .models import Qualite
from .models import Experience
from .models import Formation
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
def CreateExperience(experience,periode,domaine):
	experience, experienceCree=Experience.objects.get_or_create(experience=experience,periode=periode,domaine=domaine)
	return experience
#	return HttpResponse("experience %s du %s au %s cree" % metier.intitule, dateDebut, dateFin)
##########################
def CreateFormation(formation,periode,domaine):
	formation, formationCree = Formation.objects.get_or_create(formation=formation,periode=periode,domaine=domaine)
	return formation
