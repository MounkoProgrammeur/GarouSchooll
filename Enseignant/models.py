from django.db import models
from Accounts.models import User


class Enseignant(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    matricule = models.CharField(
        max_length=30,
        unique=True
    )

    grade = models.CharField(
        max_length=100
    )

    specialite = models.CharField(
        max_length=150
    )

    date_recrutement = models.DateField(
        null=True,
        blank=True
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.user} ({self.specialite})"