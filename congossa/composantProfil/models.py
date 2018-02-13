from django.db import models


#############################
#useless
class competence(models.Model):
	contenu = models.CharField(max_length=200)
	#carte=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		competence=cls(contenu=nom)
		return competence
#############################
#useless
class formation(models.Model):
	contenu = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		formation=cls(contenu=nom)
		return formation
#############################
#bac +
class diplome(models.Model):
	contenu = models.CharField(max_length=200)
	#carte=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		diplome=cls(contenu=nom)
		return diplome
#############################
#useless ou nb année
class experience(models.Model):
	contenu = models.CharField(max_length=200)
	#id genere automatiquement
	@classmethod
	def create (cls,content):
		experience=cls(contenu=nom)
		return experience
#############################
 #qualite?