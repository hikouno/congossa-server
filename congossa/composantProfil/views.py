#COMPOSANT OFFRE
from django.shortcuts import render
# Create your views here.
##########################
def CreateCompetence(contenu):
	competence = Competence.objects.get_or_create(contenu = contenu)
	return HttpResponse("Competence %s cree" % contenu)
##########################
def CreateNiveauEtude(duree,domaine):
	niveauEtude=NiveauEtude.objects.get_or_create(duree = duree,domaine=domaine)
	return HttpResponse("Niveau d'etude  %s %s cree" % duree, domaine)
##########################
def CreateMetier(contenu):
	metier=Metier.Create(contenu)
	metier.save()
	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateQualite(contenu):
	qualite=Qualite.objects.get_or_create(contenu)
	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateExperience(metier,dateDebut,dateFin):
	experience=Experience.objects.get_or_create(metier=metier,dateDebut=dateDebut,dateFin=dateFin)
	return HttpResponse("experience %s du %s au %s cree" % metier.intitule, dateDebut, dateFin)
##########################