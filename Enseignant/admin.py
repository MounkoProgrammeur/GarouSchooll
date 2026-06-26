from django.contrib import admin
from .models import Enseignant, InvitationEnseignant


@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = (
        "matricule", "nom", "prenom",
        "grade", "specialite", "email_personnel",
        "date_recrutement", "actif"
    )
    list_filter = ("actif", "grade", "specialite")
    search_fields = ("matricule", "nom", "prenom", "email_personnel")
    ordering = ("nom", "prenom")
    readonly_fields = ("matricule",)

    fieldsets = (
        ("Compte utilisateur", {
            "fields": ("user",)
        }),
        ("Identité", {
            "fields": ("matricule", "nom", "prenom")
        }),
        ("Informations professionnelles", {
            "fields": (
                "grade", "specialite",
                "email_personnel", "date_recrutement", "actif"
            )
        }),
    )


@admin.register(InvitationEnseignant)
class InvitationEnseignantAdmin(admin.ModelAdmin):
    list_display = (
        "enseignant", "token", "utilise",
        "date_creation", "expiration"
    )
    list_filter = ("utilise",)
    search_fields = ("enseignant__matricule", "enseignant__nom")
    readonly_fields = ("token", "date_creation")