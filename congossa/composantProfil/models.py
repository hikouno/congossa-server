from django.db import models
import datetime
#############################
#useless
class Competence(models.Model):
	contenu = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		competence=cls(contenu=nom)
		return competence
#############################
#useless
#class formation(models.Model):
#	contenu = models.CharField(max_length=200)
#id genere automatiquement
##	@classmethod
#	def create (cls,content):
#		formation=cls(contenu=nom)
#		return formation
#############################
#bac +
class NiveauEtude(models.Model):
	duree = models.CharField(max_length=200)
	domaine = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,duree,domaine):
		niveauEtude=cls(duree=duree,domaine=domaine)
		return niveauEtude
#############################
class Metier(models.Model):
	intitule=models.CharField(max_length=200)
	@classmethod
	def create (cls,intitule):
		metier=cls(intitule=intitule)
		return metier
	#id genere automatiquement
#############################
class Qualite(models.Model):
	contenu=models.CharField(max_length=200)
	@classmethod
	def create (cls,contenu):
		qualite=cls(contenu=contenu)
		return qualite
	#id genere automatiquement
	#useless ou nb année
#############################
class Experience(models.Model):
	metierPratique= models.ForeignKey(Metier, on_delete=models.CASCADE, null=True)
	dateDebut=datetime
	dateFin=datetime
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		experience=cls(contenu=nom)
		return experience
#############################
class Formation(models.Model):
	intitule=models.CharField(max_length=200)
	dateDebut=datetime
	dateFin=datetime
	#id genere automatiquement
	@classmethod
	def create(cls, intitule, dateDebut, dateFin):
		formation = cls(intitule=intitule\
			, dateDebut=dateDebut\
			, dateFin=dateFin)
		return formation
