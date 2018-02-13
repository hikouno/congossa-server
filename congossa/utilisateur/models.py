#UTILISATEUR
from django.db import models
import datetime
from django.contrib.auth.models import User
from composantProfil.models import cartePresentation


class Utilisateur(User):
	dateDeNaissance = models.CharField(max_length=200,default='null')
	localisation = models.CharField(max_length=200,default='null')
	# A voir pour le delete et le default
	carteCompetence = models.OneToOneField(cartePresentation\
		,on_delete=models.CASCADE\
		,default=cartePresentation.create("Carte de %s" % username))
	description = models.CharField(max_length=200,default='null')
	avatar = models.CharField(max_length=200,default='null')
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
		, avatar\
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
			,avatar=avatar
			,qualite=qualite
			,description=description)
	return utilisateur
