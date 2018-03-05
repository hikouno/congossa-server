from rest_framework import serializers
from composantProfil.serializers import FormationSerializer

from .models import Utilisateur

#Sérialiseur ne renvoyant que la formation de l'utilisateur.
class UtilisateurFormationSerializer(serializers.ModelSerializer):
    
    formation = FormationSerializer(many=True)
    
    class Meta:
        model = Utilisateur
        fields = ('formation',)
