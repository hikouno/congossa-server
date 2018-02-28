#OFFRE
from django.db import models
from utilisateur.models import Utilisateur
from composantProfil.models import Metier
from composantProfil.models import Experience
from composantProfil.models import Qualite
from composantProfil.models import Competence
from composantProfil.models import Formation


class Offre(models.Model):
	titre= models.CharField(max_length=200, blank=True)
	categorie = models.ForeignKey(Metier, on_delete=models.CASCADE, null=True)
	typeContrat = models.CharField(max_length=200, blank=True)
	dateDebut =  models.CharField(max_length=200, blank=True)
	dateFin = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	description = models.CharField(max_length=400, blank=True) # Plus long au cas ou

	experiencesRequises = models.ManyToManyField(Experience, blank=True)
	competencesRequises = models.ManyToManyField(Competence, blank=True)
	qualitesRequises = models.ManyToManyField(Qualite, blank=True)
	recruteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
	# Id genere automatiquement
	@classmethod
	def create (cls, titre,categorie,typeContrat,dateDebut, dateFin, city, description, experiencesRequises,competencesRequises,qualitesRequises, recruteur):
		offre=cls(titre=titre\
			,categorie=categorie\
			,typeContrat=typeContrat\
			,dateDebut=dateDebut\
			,dateFin=dateFin\
			,city=city\
			,description=description\

			,experiencesRequises=experiencesRequises\
			,competencesRequises=competencesRequises\
			,qualitesRequises=qualitesRequises\
			,recruteur=recruteur)
		return offre
###############################
class Demande(models.Model):
	categorie = models.ForeignKey(Metier, on_delete=models.CASCADE, null=True)
	typeContrat = models.CharField(max_length=200, blank=True)
	dateDebut =  models.CharField(max_length=200, blank=True)
	dateFin = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	description = models.CharField(max_length=400, blank=True) # Plus long au cas ou

	competencePossede = models.ManyToManyField(Competence, blank=True)
	qualitePossede = models.ManyToManyField(Qualite, blank=True)
	experiencePossede= models.ManyToManyField(Experience, blank=True)
	demandeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
	# Id genere automatiquement
	@classmethod
	def create (cls,categorie,typeContrat, dateDebut, dateFin, city, description, competencePossede,qualitePossede,experiencePossede,demandeur):
		demande=cls(categorie=categorie\
			,typeContrat=typeContrat\
			,dateDebut=dateDebut\
			,dateFin=dateFin\
			,city=city\
			,description=description\
			,competencePossede=competencePossede\
			,qualitePossede=qualitePossede\
			,experiencePossede=experiencePossede\
			,demandeur=demandeur)
		return demande
