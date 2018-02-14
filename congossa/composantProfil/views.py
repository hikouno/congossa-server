#COMPOSANT OFFRE
from django.shortcuts import render

# Create your views here.
##########################
def CreateCompetence(contenu):
	competence=Competence.Create(contenu)
	competence.save()
	return HttpResponse("Competence %s cree" % contenu)
##########################
def EditCompetence(competence,newContent):
	competence.contenu=newContent
	competence.save()
	return HttpResponse("Competence %s medifie" % newContent)
##########################
def CreateNiveauEtude(duree,domaine):
	niveauEtude=NiveauEtude.Create(duree,domaine)
	niveauEtude.save()
	return HttpResponse("Niveau d'etude  %s %s cree" % duree domaine)
##########################
def EditNiveauEtude(niveauEtude,duree,domaine):
	niveauEtude.duree=duree
	niveauEtude.domaine=domaine
	niveauEtude.save()
	return HttpResponse("niveauEtude %s medifie" % newContent)
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
##########################
def EditExperience(experience,metier,dateDebut,dateFin):
	experience.metier=metier
	experience.dateDebut=dateDebut
	experience.dateFin=dateFin
	experience.save()
	return HttpResponse("experience %s du %s au %s modifie" % metier.intitule dateDebut dateFin)
##########################