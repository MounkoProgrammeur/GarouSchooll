
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Etudiant', include('app.urls')),
    path('Enseignant/', include('Enseignant.urls')),
    path('Admin/', include('Admin.urls')),
    path('', include('Accounts.urls')),
]
