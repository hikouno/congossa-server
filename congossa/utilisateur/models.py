#UTILISATEUR
from django.db import models

# Create your models here.
class Utilisateur(models.Model):
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	dateDeNaissance = models.DateTimeField('dateDeNaissance')
	localisation = models.CharField(max_length=2001)
	competencePossede = models.CharField(max_length=200)
	formationPossede = models.CharField(max_length=200)
	diplomePossede =models.CharField(max_length=200)
	description = models.CharField(max_length=400) # Plus long au cas ou
	# Id genere automatiquement