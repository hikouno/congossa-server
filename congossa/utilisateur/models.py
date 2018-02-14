#UTILISATEUR
from django.db import models
import datetime
from django.contrib.auth.models import User
from composantProfil.models import NiveauEtude
from composantProfil.models import Experience
from composantProfil.models import Qualite



class Utilisateur(User):
	dateDeNaissance = models.CharField(max_length=200,default='null')
	localisation = models.CharField(max_length=200,default='null')
	# A voir pour le delete et le default
	avatar = models.CharField(max_length=200,default='null')
	qualite = models.ManyToManyField(Qualite)
	niveauEtude=models.ManyToManyField(NiveauEtude)
	experience = models.ManyToManyField(Experience)
	description = models.CharField(max_length=200,default='null')
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
	def create (cls, username, password, nom, prenom, email, dateDeNaissance, localisation, avatar, description):
		utilisateur=cls(username=username\
			,password=password\
			,date_joined=datetime.datetime.now()\
			,last_name=nom\
			,first_name=prenom\
			,email=email\
			,last_login=datetime.datetime.now()\
			,dateDeNaissance=dateDeNaissance\
			,localisation=localisation\
			,avatar=avatar\
			,description=description)
		return utilisateur

