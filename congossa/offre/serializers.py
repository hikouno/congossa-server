from rest_framework import serializers
from composantProfil.serializers import CompetenceSerializer
from composantProfil.serializers import MetierSerializer
from composantProfil.serializers import QualiteSerializer
from composantProfil.serializers import ExperienceSerializer
from composantProfil.serializers import FormationSerializer

from utilisateur.serializers import UtilisateurFormationSerializer
from utilisateur.serializers import UtilisateurBasiqueSerializer

from .models import Demande, Offre


'''class DemandeSerializer(serializers.Serializer):

    categorie = MetierSerializer()
	typeContrat = serializers.CharField(max_length=200)
	dateDebut = serializers.DateTimeField()
	dateFin = serializers.DateTimeField()
	city = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=400)

	competencePossede = models.ManyToManyField(Competence, many=True)
	qualitePossede = models.ManyToManyField(Qualite, blank=True)
	experiencePossede= models.ManyToManyField(Experience, blank=True)
	demandeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)'''

class DemandeSerializer(serializers.ModelSerializer):

    categorie = MetierSerializer()
    competencePossede = CompetenceSerializer(many=True)
    qualitePossede = QualiteSerializer(many=True)
    experiencePossede = ExperienceSerializer(many=True)
    demandeur = UtilisateurBasiqueSerializer()

    class Meta:
          model = Demande

          fields = (
                'categorie', 'typeContrat', 'dateDebut', 'dateFin', 'city', 'description', 'competencePossede', 'qualitePossede',
                'experiencePossede', 'demandeur')

          depth = 2

class OffreSerializer(serializers.ModelSerializer):

    categorie = MetierSerializer()
    competencesRequises = CompetenceSerializer(many=True)
    qualitesRequises = QualiteSerializer(many=True)
    experiencesRequises = ExperienceSerializer(many=True)
    recruteur = UtilisateurFormationSerializer()

    class Meta:
          model = Offre

          fields = (
                'titre', 'categorie', 'typeContrat', 'dateDebut', 'dateFin', 'city', 'description', 'competencesRequises', 'qualitesRequises',
                'experiencesRequises', 'recruteur')

          depth = 2
