from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi ca a l air d etre de la triche un peu
	# Routage vers les differentes fction
    path('inscription/<slug:nom>', views.inscription, name='inscription'),
    path('desincription/<slug:nom>', views.desincription, name='desincription'),
    path('rechercher/<slug:nom>', views.rechercher, name='rechercher'),

]