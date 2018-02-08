#UTILISATEUR
from django.db import models
import datetime
from django.contrib.auth.models import User

class Utilisateur(User):
	dateDeNaissance = models.CharField(max_length=200,default='null')
	localisation = models.CharField(max_length=200,default='null')
	# Remplace par des objts
	competencePossede = models.CharField(max_length=200,default='null')
	formationPossede = models.CharField(max_length=200,default='null')
	diplomePossede =models.CharField(max_length=200,default='null')
	description = models.CharField(max_length=200,default='null')
	avatar = models.CharField(max_length=200,default='null')
	experiencePossede = models.CharField(max_length=200,default='null')
	qualite = models.CharField(max_length=200,default='null')
	#listeOffre
	# Champs genere par heritage d user
	# username = username (Obligatoire + Sert de clef unique)
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
	def create (cls\
		, username\
		, password\
		, nom\
		, prenom\
		, email\
		, dateDeNaissance\
		, localisation\
		, competencePossede\
		, formationPossede\
		, diplomePossede\
		, avatar\
		, experiencePossede\
		, qualite\
		,description):
		utilisateur=cls(username=username\
			,password=password\
			,date_joined=datetime.datetime.now()\
			,last_name=nom\
			,first_name=prenom\
			,email=email\
			,dateDeNaissance=dateDeNaissance\
			,last_login=datetime.datetime.now()\
			,localisation=localisation\
			,competencePossede=competencePossede\
			,formationPossede=formationPossede\
			,diplomePossede=diplomePossede\
			,avatar=avatar
			,experiencePossede=experiencePossede
			,qualite=qualite
			,description=description)
		return utilisateur