#OFFRE
from django.urls import path

from . import views
from utilisateur.models import Utilisateur

urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('<int:idRecruteur>/ajoutOffre/<slug:titre>/<slug:metier>/<slug:typeContrat>/<slug:localisation>/<slug:diplomeDemande>/<slug:dateDebut>/<slug:dureeContrat>/<slug:description>'\
    	, views.ajoutOffre\
    	, name='ajoutOffre'),
    path('<int:idDemandeur>/ajoutDemande/<slug:metier>/<slug:typeContrat>/<slug:localisation>/<slug:diplomePossede>/<slug:dateDebut>/<slug:dureeDisponibilite>/<slug:description>'\
    	, views.ajoutDemande\
    	, name='ajoutDemande'),
    path('<int:idUser>/voirAnnonce/<slug:nom>', views.voirAnnonce, name='voirAnnonce'),

]