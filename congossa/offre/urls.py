from django.urls import path

from . import views


urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('ajoutOffre/<slug:nom>', views.ajoutOffre, name='ajoutOffre'),
    path('ajoutDemande/<slug:nom>', views.ajoutDemande, name='ajoutDemande'),
    path('voirMatch/<slug:nom>', views.voirMatch, name='voirMatch'),

]