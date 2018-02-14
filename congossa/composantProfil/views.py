#COMPOSANT OFFRE
from django.shortcuts import render

# Create your views here.
def CreateCompetence(contenu):
	competence=Competence.Create(contenu)
	competence.save()
	return HttpResponse("Competence %s cree" % contenu)
def CreateNiveauEtude(duree,domaine):
	niveauEtude=Competence.Create(duree,domaine)
	niveauEtude.save()
	return HttpResponse("Niveau d'etude  %s %s cree" % duree domaine)
def CreateMetier(contenu):
	metier=Competence.Create(contenu)
	metier.save()
	return HttpResponse("Metier %s cree" % contenu)