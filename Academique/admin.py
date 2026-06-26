from django.contrib import admin
from .models import (
    Cours,
    Seance,
    Evaluation,
    Note,
    Presence,
)


class SeanceInline(admin.TabularInline):
    model = Seance
    extra = 0


class EvaluationInline(admin.TabularInline):
    model = Evaluation
    extra = 0


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = (
        "code", "nom", "responsable",
        "classe", "semestre", "credit"
    )
    list_filter = ("semestre", "classe")
    search_fields = ("code", "nom")
    ordering = ("code",)
    inlines = [SeanceInline, EvaluationInline]

    fieldsets = (
        ("Identification", {
            "fields": ("code", "nom", "responsable")
        }),
        ("Organisation", {
            "fields": ("classe", "semestre",  "credit")
        }),
    )


@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = (
        "cours", "date",
        "heure_debut", "heure_fin"
    )
    list_filter = ("cours", "date")
    search_fields = ("cours__nom", "cours__code")
    ordering = ("-date",)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        "titre", "cours", "type",
        "coefficient", "date_evaluation", "publie"
    )
    list_filter = ("type", "publie", "cours")
    search_fields = ("titre", "cours__nom")
    ordering = ("-date_evaluation",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "etudiant", "evaluation", "note", "appreciation"
    )
    list_filter = ("evaluation__cours", "evaluation__type")
    search_fields = (
        "etudiant__matricule", "etudiant__nom",
        "evaluation__titre"
    )


@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ("etudiant", "seance", "statut")
    list_filter = ("statut", "seance__cours")
    search_fields = (
        "etudiant__matricule", "etudiant__nom",
        "seance__cours__nom"
    )