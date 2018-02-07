#UTILISATEUR
from django.db import models
from django.contrib.auth.models import User

class Utilisateur(User):
	dateDeNaissance = models.CharField(max_length=200,null=True)
	localisation = models.CharField(max_length=200,null=True)
	competencePossede = models.CharField(max_length=200,null=True)
	formationPossede = models.CharField(max_length=200,null=True)
	diplomePossede =models.CharField(max_length=200,null=True)
	description = models.CharField(max_length=400,null=True) # Plus long au cas ou
	# Id genere automatiquement
	# Champs genere par heritage d user
	# login = String (Obligatoire)
	# password = String (Obligatoire)
	# lastLogin = Date
	# dateInscription = Date
	# nom = String
	# prenom = String
	# email = String
	# membreDuStaff = Boolean (False par default)
	# superUser = Boolean (False par default)
	# actif = Boolean (True par default)
	# permissions = ? 
	# Group = ? (Vide par default)