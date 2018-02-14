from django.db import models

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
	intitule:models.CharField(max_length=200)
	#id genere automatiquement
#useless ou nb année
class Experience(models.Model):
	contenu = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		experience=cls(contenu=nom)
		return experience
#############################
class Qualite(models.Model):
	contenu=models.CharField(max_length=200)
	#id genere automatiquement