from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect


def home(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user is not None:

            if not user.is_active:
                return render(
                    request,
                    "home.html",
                    {
                        "erreur": "Compte non activé"
                    }
                )

            login(request, user)

            if user.type_utilisateur == "ADMIN":
                return redirect("dashboard_admin")

            elif user.type_utilisateur == "ENSEIGNANT":
                return redirect("dashboard_enseignant")

            elif user.type_utilisateur == "ETUDIANT":
                return redirect("dashboard_etudiant")

        else:

            return render(
                request,
                "home.html",
                {
                    "erreur": "Email ou mot de passe incorrect"
                }
            )

    return render(request, "home.html")