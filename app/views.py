from django.shortcuts import render



def Dashbord(request):
    
    return render(request, 'Etudiant/dashbord.html')

def Mes_Notes(request):
    return render(request, 'Etudiant/notes.html')

def Performances(request):
    return render(request, 'Etudiant/performances.html')


def Paiement1(request):
    return render(request, 'Etudiant/paiement 1.html')

def Paiement2(request):
    return render(request, 'Etudiant/paiement 2.html')

def Moratoire(request):
    return render(request, 'Etudiant/Moratoire.html')

def Document(request):
    return render(request, 'Etudiant/documents.html')

def Notification(request):
    return render(request, 'Etudiant/notification.html')

def Parametres(request):
    return render(request, 'Etudiant/parametres.html')

def Profil(request):
    return render(request, 'Etudiant/profil.html')
