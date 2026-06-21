from django.shortcuts import render


def Dashbord(request):
    return render(request, 'Teacher/dashbord.html')

def Notes(request):
    return render(request, 'Teacher/notes.html')

def Cours(request):
    return render(request, 'Teacher/mes_cours.html')

def Etudiant(request):
    return render(request, 'Teacher/etudiants.html')

def Presences(request):
    return render(request, 'Teacher/presences.html')

def Annonces(request):
    return render(request, 'Teacher/annonces.html')

def Parametres(request):
    return render(request, 'Teacher/parametres.html')