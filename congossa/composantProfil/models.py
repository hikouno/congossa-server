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
	titre=models.CharField(max_length=200);
	domaine= models.CharField(max_length=200)
	duree=models.DurationField(null=True)
	#id genere automatiquement

	@classmethod
	def create (cls,titre, domaine, duree):
		experience=cls(titre=titre,
			domaine=domaine,
			duree=duree)
		return experience
#############################
class Formation(models.Model):
	titre=models.CharField(max_length=200);
	domaine= models.CharField(max_length=200)
	duree=models.DurationField(null=True)
	#id genere automatiquement

	@classmethod
	def create (cls,titre, domaine, duree):
		formation=cls(titre=titre,
			domaine=domaine,
			duree=duree)
		return formation
