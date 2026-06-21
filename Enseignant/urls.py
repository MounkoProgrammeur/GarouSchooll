from django.urls import path
from . import views
urlpatterns = [
    path('', views.Dashbord, name='dashboard'),
    path('notes/', views.Notes, name='notes'),
    path('cours/', views.Cours, name='cours'),
    path('etudiants/', views.Etudiant, name='etudiants'),
    path('presences/', views.Presences, name='presences'),
    path('annonces/', views.Annonces, name='annonces'),
    path('parametres/', views.Parametres, name='parametres'),
]
