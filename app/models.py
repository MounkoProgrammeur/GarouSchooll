from django.db import models

from Accounts.models import User
from Admin.models import (
    Classe,
    AnneeAcademique
)


class Etudiant(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    matricule = models.CharField(
        max_length=30,
        unique=True
    )

    date_naissance = models.DateField()

    lieu_naissance = models.CharField(
        max_length=150
    )

    def __str__(self):
        return f"{self.user}"


class ValidationEtudiant(models.Model):

    STATUS = (
        ("EN_ATTENTE", "En attente"),
        ("VALIDE", "Validé"),
        ("REJETE", "Rejeté"),
    )

    etudiant = models.OneToOneField(
        Etudiant,
        on_delete=models.CASCADE
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUS,
        default="EN_ATTENTE"
    )

    date_validation = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.etudiant} - {self.statut}"


class Inscription(models.Model):

    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE
    )

    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE
    )

    annee = models.ForeignKey(
        AnneeAcademique,
        on_delete=models.CASCADE
    )

    date_inscription = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.etudiant} - {self.classe}"