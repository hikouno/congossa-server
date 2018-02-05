#UTILISATEUR
from django.urls import path

from . import views


urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('voirProfil/<slug:nom>', views.voirProfil, name='voirProfil'),
]