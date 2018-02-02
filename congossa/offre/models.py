from django.db import models


class Offre(models.Model):
	metieR = models.CharField(max_length=200)
	typeContrat = models.CharField(max_length=200)
	localisation = models.CharField(max_length=200)
	competenceRequise = models.CharField(max_length=200)
	diplomeRequis =models.CharField(max_length=200)
	dateDebut =  models.DateTimeField('dateDebut')
	dureeContrat = models.IntegerField(default=0)
	description = models.CharField(max_length=400) # Plus long au cas ou
	# recruteur = useurEmployeur
	# Id genere automatiquement

class Demande(models.Model):
	metier = models.CharField(max_length=200)
	typeContrat = models.CharField(max_length=200)
	localisation = models.CharField(max_length=2001)
	competencePossede = models.CharField(max_length=200)
	diplomePossede =models.CharField(max_length=200)
	dateDebut =  models.DateTimeField('dateDebut')
	dureeDisponibilite = models.CharField(max_length=200) # pas sur 
	description = models.CharField(max_length=400) # Plus long au cas ou
	# demandeur = useurDemandeur
	# Id genere automatiquement