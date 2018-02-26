#OFFRE
from django.urls import path

from . import views
from utilisateur.models import Utilisateur

urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String ca a l air d etre de la triche un peu
    path('allDialogUser/', views.allDialogUser, name='allDialogUser'),
    path('newDialog/', views.newDialog, name='newdialog'),
    path('getLastMessage/', views.getLastMessage, name='getlastmessage'),
    path('getDialog/', views.getDialog, name='getdialog'),
    path('addMessage/', views.addMessage, name='addmessage'),
]
