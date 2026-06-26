from django.contrib import admin
from .models import (
    AnneeAcademique,
    Faculte,
    Departement,
    Filiere,
    Niveau,
    Classe,
    Annonce,
    DocumentCours,
    AffectationCours,
)


@admin.register(AnneeAcademique)
class AnneeAcademiqueAdmin(admin.ModelAdmin):
    list_display = ("libelle", "active")
    list_filter = ("active",)
    search_fields = ("libelle",)


@admin.register(Faculte)
class FaculteAdmin(admin.ModelAdmin):
    list_display = ("code", "nom")
    search_fields = ("code", "nom")


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ("nom", "faculte")
    list_filter = ("faculte",)
    search_fields = ("nom",)


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ("nom", "departement")
    list_filter = ("departement",)
    search_fields = ("nom",)


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ("nom", "filiere", "niveau", "annee")
    list_filter = ("annee", "niveau", "filiere")
    search_fields = ("nom",)


@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ("titre", "enseignant", "date_publication")
    list_filter = ("date_publication",)
    search_fields = ("titre", "message")
    filter_horizontal = ("classes",)
    readonly_fields = ("date_publication",)


@admin.register(DocumentCours)
class DocumentCoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "cours", "date_ajout")
    list_filter = ("date_ajout",)
    search_fields = ("titre",)
    readonly_fields = ("date_ajout",)


@admin.register(AffectationCours)
class AffectationCoursAdmin(admin.ModelAdmin):
    list_display = (
        "enseignant", "cours", "annee_academique", "date_affectation"
    )
    list_filter = ("annee_academique",)
    search_fields = ("enseignant__nom", "cours__nom")
    readonly_fields = ("date_affectation",)