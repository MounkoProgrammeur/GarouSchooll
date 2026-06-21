from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('Dashbord/', views.Dashbord, name='dash'),
    path('notes/', views.Mes_Notes, name='note'),
    path('perf/', views.Performances, name='performances'),
    path('Tranche1/', views.Paiement1, name='paiement1'),
    path('Tranche2/', views.Paiement2, name='paiement2'), 
    path('Moratoire/', views.Moratoire, name='moratoire'), 
    path('document/', views.Document, name='documents'),
    path('notif/', views.Notification, name='notifications'),
    path('parametres/', views.Parametres, name='parametre'),
    path('profil/', views.Profil, name='profil'),
    
]
