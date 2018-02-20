#OFFRE
from django.db import models
from utilisateur.models import Utilisateur
from composantProfil.models import Metier
from composantProfil.models import NiveauEtude
from composantProfil.models import Experience
from composantProfil.models import Qualite

class Offre(models.Model):
	titre= models.CharField(max_length=200, null=True, blank=True)
	metier = models.ForeignKey(Metier, on_delete=models.CASCADE, null=True, blank=True)
	typeContrat = models.CharField(max_length=200, null=True, blank=True)
	localisation = models.CharField(max_length=200, null=True, blank=True)
	competenceRequise = models.CharField(max_length=200, null=True, blank=True)
	diplomeRequis =models.ManyToManyField(NiveauEtude, blank=True)
	dateDebut =  models.CharField(max_length=200, null=True, blank=True)
	dureeContrat = models.CharField(max_length=200, null=True, blank=True)
	experienceRequise= models.ManyToManyField(Experience, blank=True)
	description = models.CharField(max_length=400, null=True, blank=True) # Plus long au cas ou
	recruteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)
	# Id genere automatiquement
	@classmethod
	def create (cls, titre,metier,typeContrat,localisation,competenceRequise,diplomeRequis,dateDebut,dureeContrat,experienceRequise,description,recruteur):
		offre=cls(titre=titre\
			,metier=metier\
			,typeContrat=typeContrat\
			,localisation=localisation\
			,competenceRequise=competenceRequise\
			,diplomeRequis=diplomeRequis\
			,dateDebut=dateDebut\
			,dureeContrat=dureeContrat\
			,experienceRequise=experienceRequise\
			,description=description\
			,recruteur=recruteur)
		return offre
###############################
class Demande(models.Model):
	categorie = models.CharField(max_length=200)
	typeContrat = models.CharField(max_length=200)
	dateDebut =  models.CharField(max_length=200)
	dateFin = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	description = models.CharField(max_length=400) # Plus long au cas ou

	competencePossede = models.ManyToManyField(Competence)
	qualitePossede = models.ManyToManyField(Qualite)
	formations = models.ManyToManyField(Formation)
	diplomePossede =models.ManyToManyField(NiveauEtude)
	experiencePossede= models.ManyToManyField(Experience)
	demandeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
	# Id genere automatiquement
	@classmethod
	def create (cls, titre,categorie,typeContrat,dateFin, dateDebut, city, descritpion, competencePossede,qualitePossede,diplomePossede,experiencePossede,dateDebut,dureeDisponibilite,description,demandeur):
		demande=cls(titre=titre\
			,categorie=categorie\
			,typeContrat=typeContrat\
			,dateDebut=dateDebut\
			,dateFin=dateFin\
			,city=city\
			,description=description\
			,competencePossede=competencePossede\
			,qualitePossede=qualitePossede\

			,diplomePossede=diplomePossede\
			,experiencePossede=experiencePossede\
			,dureeDisponibilite=dureeDisponibilite\
			,description=description\
			,demandeur=demandeur)
		return demande
