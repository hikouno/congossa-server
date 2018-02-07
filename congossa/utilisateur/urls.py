#UTILISATEUR
from django.urls import path

from . import views


urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('<int:idUser>/voirProfil/<slug:nom>', views.voirProfil, name='voirProfil'),
    path('login/<slug:nomDeCompte>/<slug/motDePasse>',views.login, name='login'),
    path('register/'\
    	+ '<slug:nomDeCompte>/'\
    	+ '<slug/motDePasse>/'\
    	+ '<slug/dateInscription>/'\
    	+ '<slug/nom>/'\
    	+ '<slug/prenom>/'\
    	+ '<slug/email>/'\
    	+ '<slug/dateDeNaissance>/'\
    	+ '<slug/localisation>/'\
    	+ '<slug/competencePossede>/'\
    	+ '<slug/formationPossede>'\
    	+ '<slug/diplomePossede>'\
    	+ '<slug/description>'\
    	, views.register, name='register'),
]