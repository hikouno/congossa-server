#COMPOSANT OFFRE
from django.shortcuts import render

# Create your views here.
##########################
def CreateCompetence(contenu):
	competence=Competence.Create(contenu)
	competence.save()
	return HttpResponse("Competence %s cree" % contenu)
##########################
def CreateNiveauEtude(duree,domaine):
	niveauEtude=NiveauEtude.Create(duree,domaine)
	niveauEtude.save()
	return HttpResponse("Niveau d'etude  %s %s cree" % duree domaine)
##########################
def CreateMetier(contenu):
	metier=Metier.Create(contenu)
	metier.save()
	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateQualite(contenu):
	qualite=Qualite.Create(contenu)
	qualite.save()
	return HttpResponse("Metier %s cree" % contenu)
##########################
def CreateExperience(metier,dateDebut,dateFin):
	experience=Experience.Create(metier,dateDebut,dateFin)
	experience.save()
	return HttpResponse("experience %s du %s au %s cree" % metier.intitule dateDebut dateFin)