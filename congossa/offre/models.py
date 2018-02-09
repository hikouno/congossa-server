#OFFRE
from django.db import models
from utilisateur.models import Utilisateur


class Offre(models.Model):
	titre= models.CharField(max_length=200)
	metier = models.CharField(max_length=200)
	typeContrat = models.CharField(max_length=200)
	localisation = models.CharField(max_length=200)
	competenceRequise = models.CharField(max_length=200)
	diplomeRequis =models.CharField(max_length=200)
	dateDebut =  models.CharField(max_length=200)
	dureeContrat = models.CharField(max_length=200)
	description = models.CharField(max_length=400) # Plus long au cas ou
	recruteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
	# Id genere automatiquement
	@classmethod
	def create (cls, titre,metier,typeContrat,localisation,competenceRequise,diplomeRequis,dateDebut,dureeContrat,description,recruteur):
		offre=cls(titre=titre\
			,metier=metier\
			,typeContrat=typeContrat\
			,localisation=localisation\
			,competenceRequise=competenceRequise\
			,diplomeRequis=diplomeRequis\
			,dateDebut=dateDebut\
			,dureeContrat=dureeContrat\
			,description=description\
			,recruteur=recruteur)
		return offre
class Demande(models.Model):
	metier = models.CharField(max_length=200)
	typeContrat = models.CharField(max_length=200)
	localisation = models.CharField(max_length=2001)
	competencePossede = models.CharField(max_length=200)
	diplomePossede =models.CharField(max_length=200)
	dateDebut =  models.CharField(max_length=200)
	dureeDisponibilite = models.CharField(max_length=200) # pas sur
	description = models.CharField(max_length=400) # Plus long au cas ou
	demandeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
	# Id genere automatiquement