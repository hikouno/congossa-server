#COMPOSANT OFFRE
from django.shortcuts import render
from .models import Competence
from .models import Qualite
from .models import Experience
from .models import Formation
from .models import Metier

# Create your views here.
##########################
def CreateMetier(intitule):
	metier,metierCree = Metier.objects.get_or_create(intitule=intitule)
	return metier
def CreateCompetence(contenue):
	competence, competenceCree = Competence.objects.get_or_create(contenu=contenue)
	return competence
##########################
def CreateQualite(contenue):
	qualite, qualiteCree=Qualite.objects.get_or_create(contenu=contenue)
	return qualite
#	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateExperience(titre,duree,domaine):
	dom=CreateMetier(domaine)
	experience, experienceCree=Experience.objects.get_or_create(titre=titre,domaine=dom,duree=duree)
	return experience
#	return HttpResponse("experience %s du %s au %s cree" % metier.intitule, dateDebut, dateFin)
##########################
def CreateFormation(titre,duree,domaine):
	#dom=CreateMetier(domaine)
	formation, formationCree = Formation.objects.get_or_create(titre=titre,domaine=domaine,duree=duree)
	print(formation)
	return formation
