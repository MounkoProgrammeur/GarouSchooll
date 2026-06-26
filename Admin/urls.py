from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),
    
    
     path(
        "enseignants/",
        views.liste_enseignants,
        name="liste_enseignants"
    ),

    path(
        "enseignants/ajouter/",
        views.ajouter_enseignant,
        name="ajouter_enseignant"
    ),

    path(
        "enseignants/<int:id>/modifier/",
        views.modifier_enseignant,
        name="modifier_enseignant"
    ),

    path(
        "enseignants/<int:id>/supprimer/",
        views.supprimer_enseignant,
        name="supprimer_enseignant"
    ),
]
