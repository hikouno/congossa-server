#UTILISATEUR
from django.db import models
from django.contrib.auth.models import User

class Utilisateur(User):
	dateDeNaissance = models.CharField(max_length=200,default='null')
	localisation = models.CharField(max_length=200,default='null')
	competencePossede = models.CharField(max_length=200,default='null')
	formationPossede = models.CharField(max_length=200,default='null')
	diplomePossede =models.CharField(max_length=200,default='null')
	description = models.CharField(max_length=400,default='null') # Plus long au cas ou
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
	#########################################################
	# Un constructeur
	@classmethod
	def create (cls, login, password, dateInscription,nom,prenom,email,dateDeNaissance,localisation,competencePossede,formationPossede,diplomePossede,description):
		utilisateur=cls(login=login\
			,password=password\
			,dateInscription=dateInscription\
			,nom=nom\
			,prenom=prenom\
			,email=email\
			,dateDeNaissance=dateDeNaissance\
			,localisation=localisation\
			,competencePossede=competencePossede\
			,formationPossede=formationPossede\
			,diplomePossede=diplomePossede\
			,description=description)
		return utilisateur