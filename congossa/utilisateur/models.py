#UTILISATEUR
from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from composantProfil.models import Experience
from composantProfil.models import Formation
from composantProfil.models import Qualite
from composantProfil.models import Competence

class Utilisateur(AbstractUser):

	dateDeNaissance = models.CharField(max_length=200,default='null')
	localisation = models.CharField(max_length=200,default='null')
	# A voir pour le delete et le default
	avatar = models.CharField(max_length=2000,default='null')
	competence = models.ManyToManyField(Competence)
	qualite = models.ManyToManyField(Qualite)
	formation=models.ManyToManyField(Formation)
	experience = models.ManyToManyField(Experience)
	description = models.CharField(max_length=200,default='null')
	sexe = models.CharField(max_length=200,default='null')
	telephone = models.CharField(max_length=200,default='null')
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