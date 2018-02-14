#OFFRE
from django.urls import path

from . import views
from utilisateur.models import Utilisateur

urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('ajoutOffre/', views.ajoutOffre, name='ajoutOffre'),
    path('ajoutDemande/', views.ajoutDemande, name='ajoutDemande'),
    path('voirAnnonce/', views.voirAnnonce, name='voirAnnonce'),

]