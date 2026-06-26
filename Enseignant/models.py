from django.db import models
from Accounts.models import User
import uuid


class Enseignant(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    matricule = models.CharField(
        max_length=30,
        unique=True
    )

    nom = models.CharField(
        max_length=100
    )

    prenom = models.CharField(
        max_length=100
    )

    grade = models.CharField(
        max_length=100
    )

    specialite = models.CharField(
        max_length=150
    )

    email_personnel = models.EmailField()

    date_recrutement = models.DateField(
        null=True,
        blank=True
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    
class InvitationEnseignant(models.Model):
    
    enseignant = models.OneToOneField(
        Enseignant,
        on_delete=models.CASCADE
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    utilise = models.BooleanField(
        default=False
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    expiration = models.DateTimeField()

    def __str__(self):
        return self.enseignant.matricule