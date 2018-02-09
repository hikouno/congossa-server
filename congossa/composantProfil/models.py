from django.db import models

# Create your models here.
class cartePresentation(models.Model):
	#Pour le contenu jsp
	name = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,nom):
		carte=cls(name=nom)
		return carte
#############################
class competence(models.Model):
	contenu = models.CharField(max_length=200)
	carte=models.ForeignKey(cartePresentation, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		competence=cls(contenu=nom)
		return competence
#############################
class formation(models.Model):
	contenu = models.CharField(max_length=200)
	carte=models.ForeignKey(cartePresentation, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		formation=cls(contenu=nom)
		return formation
#############################
class diplome(models.Model):
	contenu = models.CharField(max_length=200)
	carte=models.ForeignKey(cartePresentation, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		diplome=cls(contenu=nom)
		return diplome
#############################
class experience(models.Model):
	contenu = models.CharField(max_length=200)
	carte=models.ForeignKey(cartePresentation, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		experience=cls(contenu=nom)
		return experience
#############################
 #qualite?