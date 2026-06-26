from django.shortcuts import render, redirect
from Enseignant.models import Enseignant
from django.shortcuts import get_object_or_404



def dashboard_admin(request):
    return render(request, "Admin/app.html")


def liste_enseignants(request):

    enseignants = Enseignant.objects.all()

    return render(
        request,
        "Admin/enseignants/liste.html", {"enseignants": enseignants })

def ajouter_enseignant(request):
    
    if request.method == "POST":

        Enseignant.objects.create(
            matricule=request.POST.get("matricule"),
            nom=request.POST.get("nom"),
            prenom=request.POST.get("prenom"),
            grade=request.POST.get("grade"),
            specialite=request.POST.get("specialite"),
            email_personnel=request.POST.get("email")
        )

        return redirect("liste_enseignants")

    return render( request, "Admin/enseignants/ajouter.html")
def modifier_enseignant(request, id):
    
    enseignant = get_object_or_404( Enseignant,id=id)

    if request.method == "POST":

        enseignant.nom = request.POST.get("nom")
        enseignant.prenom = request.POST.get("prenom")
        enseignant.grade = request.POST.get("grade")
        enseignant.specialite = request.POST.get("specialite")
        enseignant.email_personnel = request.POST.get("email")

        enseignant.save()

        return redirect("liste_enseignants")

    return render( request, "Admin/enseignants/modifier.html", {"enseignant": enseignant})
    
def supprimer_enseignant(request, id):
    
    enseignant = get_object_or_404(Enseignant, id=id)

    enseignant.delete()

    return redirect("liste_enseignants")