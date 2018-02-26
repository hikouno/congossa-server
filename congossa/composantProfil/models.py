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
	metier= models.CharField(max_length=200)
	dateDebut=models.CharField(max_length=200, blank=True)
	dateFin=models.CharField(max_length=200, blank=True)
	#id genere automatiquement

	@classmethod
	def create (cls,metier, dateDebut, dateFin):
		experience=cls(metier=metier,
			dateDebut=dateDebut,
			dateFin=dateFin)
		return experience
#############################
class Formation(models.Model):
	intitule=models.CharField(max_length=200)
	duree = models.CharField(max_length=200, blank=True)
	#id genere automatiquement
	@classmethod
	def create(cls, intitule, duree):
		formation = cls(intitule=intitule\
			, duree=duree)
		return formation
