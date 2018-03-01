from rest_framework import serializers

from .models import Competence, Metier, Qualite, Experience, Formation

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('contenu',)

#############################
class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = ('intitule',)

#############################
class QualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualite
        fields = ('contenu',)

#############################
class ExperienceSerializer(serializers.ModelSerializer):
    
    domaine = MetierSerializer()
    
    class Meta:
        model = Experience
        fields = ('titre', 'domaine', 'duree')
        
        depth = 2

#############################
class FormationSerializer(serializers.ModelSerializer):
    
    domaine = MetierSerializer()
    
    class Meta:
        model = Formation
        fields = ('titre', 'domaine', 'duree')
        
        depth = 2
