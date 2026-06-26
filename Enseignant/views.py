from django.shortcuts import render, redirect
from .models import InvitationEnseignant
from django.contrib.auth.decorators import login_required
from Accounts.models import User

from django.contrib.auth import login
from django.utils import timezone
from .models import InvitationEnseignant





@login_required
def Dashbord(request):
    if request.user.type_utilisateur != "ENSEIGNANT":
        return redirect("home")
    
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




def activation_compte(request, token):
    
    try:

        invitation = InvitationEnseignant.objects.get(
            token=token,
            utilise=False
        )

    except InvitationEnseignant.DoesNotExist:

        return render(
            request,
            "Teacher/lien_invalide.html"
        )

    if invitation.expiration < timezone.now():

        return render(
            request,
            "Teacher/lien_invalide.html"
        )

    enseignant = invitation.enseignant

    if enseignant.user:

        return render(
            request,
            "Teacher/lien_invalide.html"
        )

    if request.method == "POST":

        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")

        if password != confirmation:

            return render(
                request,
                "Teacher/activation.html",
                {
                    "erreur": "Les mots de passe ne correspondent pas"
                }
            )

        user = User.objects.create_user(
            email=enseignant.email_personnel,
            password=password,
            nom=enseignant.nom,
            prenom=enseignant.prenom,
            type_utilisateur="ENSEIGNANT",
            is_active=True
        )

        enseignant.user = user
        enseignant.save()

        invitation.utilise = True
        invitation.save()

        login(request, user)

        return redirect("dashboard_enseignant")

    return render(
        request,
        "Teacher/activation.html"
    )