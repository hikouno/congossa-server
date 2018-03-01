#UTILISATEUR
from django.urls import path
from . import views


urlpatterns = [
	# Routage vers les differentes fction
    path('', views.index, name='index'),
	# Slug pour les string jsp pourquoi pas String
    path('voirProfil/<slug:nom>', views.voirProfil, name='voirProfil'),
    # Mettre le mdp dans un post serait mieux mais pour tester les get c est pas mal
    path('login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('consulterSonProfil/<slug:nomDeCompte>',views.consulterSonProfil,name='consulterSonProfil'),
    path('editerSonProfil/'\
        + '<slug:login>/'\
        + '<slug:nom>/'\
        + '<slug:prenom>/'\
        + '<slug:email>/'\
        + '<slug:dateDeNaissance>/'\
        + '<slug:localisation>/'\
        + '<slug:avatar>/'\
        + '<slug:qualite>/'\
        + '<slug:description>/',views.editerSonProfil,name='editerSonProfil'),
    path('changerMdp/'\
        + '<slug:login>/'\
        + '<slug:nouveauMotDePasse>',views.changerMdp,name='changerMdp'),
    path('changerNom/',views.changerNom,name='changerNom'),
    path('changerPrenom/',views.changerPrenom,name='changerPrenom'),
    path('changerSexe/',views.changerSexe,name='changerSexe'),
    path('changerMail/',views.changerMail,name='changerMail'),
    path('changerDateDeNaissance/',views.changerDateDeNaissance,name='changerDateDeNaissance'),
    path('changeTelephone/',views.changeTelephone,name='changeTelephone'),
    path('changeDescription/',views.changeDescription,name='changeDescription'),
    path('changeQualite/',views.changeQualite,name='changeQualite'),
    path('changeCompetence/',views.changeCompetence,name='changeCompetence'),
    path('changeExperienceFormation/',views.changeExperienceFormation,name='changeExperienceFormation')
]
