from django.contrib import admin
from .models import (
    Etudiant,
    Inscription,
    Paiement,
    DocumentAdministratif,
    CompteurMatricule,
    ActivationEtudiant,
)


class InscriptionInline(admin.TabularInline):
    model = Inscription
    extra = 0
    readonly_fields = ("date_inscription",)


class PaiementInline(admin.TabularInline):
    model = Paiement
    extra = 0
    readonly_fields = ("date_soumission",)


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = (
        "matricule", "nom", "prenom",
        "date_naissance", "lieu_naissance", "date_creation"
    )
    search_fields = ("matricule", "nom", "prenom")
    ordering = ("nom", "prenom")
    readonly_fields = ("matricule", "date_creation")
    inlines = [InscriptionInline, PaiementInline]

    fieldsets = (
        ("Compte utilisateur", {
            "fields": ("user",)
        }),
        ("Identité", {
            "fields": (
                "matricule", "nom", "prenom",
                "date_naissance", "lieu_naissance"
            )
        }),
        ("Métadonnées", {
            "fields": ("date_creation",),
            "classes": ("collapse",)
        }),
    )


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "etudiant", "classe", "annee",
        "date_inscription", "active"
    )
    list_filter = ("annee", "classe", "active")
    search_fields = ("etudiant__matricule", "etudiant__nom")
    readonly_fields = ("date_inscription",)


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = (
        "etudiant", "annee", "tranche",
        "montant", "statut", "date_soumission", "date_validation"
    )
    list_filter = ("statut", "tranche", "annee")
    search_fields = ("etudiant__matricule", "etudiant__nom")
    readonly_fields = ("date_soumission",)

    fieldsets = (
        ("Étudiant & Année", {
            "fields": ("etudiant", "annee")
        }),
        ("Paiement", {
            "fields": ("tranche", "montant", "recu")
        }),
        ("Validation", {
            "fields": ("statut", "date_soumission", "date_validation")
        }),
    )


@admin.register(DocumentAdministratif)
class DocumentAdministratifAdmin(admin.ModelAdmin):
    list_display = (
        "titre", "etudiant", "type_document", "date_ajout"
    )
    list_filter = ("type_document",)
    search_fields = ("titre", "etudiant__matricule", "etudiant__nom")
    readonly_fields = ("date_ajout",)


@admin.register(CompteurMatricule)
class CompteurMatriculeAdmin(admin.ModelAdmin):
    list_display = ("annee", "dernier_numero")


@admin.register(ActivationEtudiant)
class ActivationEtudiantAdmin(admin.ModelAdmin):
    list_display = (
        "etudiant", "token", "utilise", "date_creation"
    )
    list_filter = ("utilise",)
    search_fields = ("etudiant__matricule", "etudiant__nom")
    readonly_fields = ("token", "date_creation")