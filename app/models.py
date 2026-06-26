from django.db import models
import uuid
from django.utils import timezone
from Accounts.models import User
from Admin.models import (
    Classe,
    AnneeAcademique
)


class Etudiant(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    matricule = models.CharField(
        max_length=30,
        unique=True,
        editable=False
    )

    nom = models.CharField(
        max_length=100
    )

    prenom = models.CharField(
        max_length=100
    )

    date_naissance = models.DateField()

    lieu_naissance = models.CharField(
        max_length=150
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"


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
    
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.etudiant} - {self.classe}"


class Paiement(models.Model):
    """
    Paiement de scolarité (1ère tranche, 2ème tranche
    ou moratoire) avec preuve de paiement uploadée par
    l'étudiant et validation par le gestionnaire.
    """

    TRANCHE_CHOICES = (
        ("TRANCHE1", "1ère tranche"),
        ("TRANCHE2", "2ème tranche"),
        ("MORATOIRE", "Moratoire"),
    )

    STATUT_CHOICES = (
        ("EN_ATTENTE", "En attente"),
        ("VALIDE", "Validé"),
    )

    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE
    )

    annee = models.ForeignKey(
        AnneeAcademique,
        on_delete=models.CASCADE
    )

    tranche = models.CharField(
        max_length=20,
        choices=TRANCHE_CHOICES
    )

    montant = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    recu = models.FileField(
        upload_to="paiements/"
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="EN_ATTENTE"
    )

    date_soumission = models.DateTimeField(
        auto_now_add=True
    )

    date_validation = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.etudiant} - {self.tranche} ({self.statut})"


class DocumentAdministratif(models.Model):
    """
    Documents administratifs de l'étudiant : certificat
    de scolarité, attestation d'inscription, reçus de
    paiement téléchargeables, etc.
    """

    TYPE_CHOICES = (
        ("CERTIFICAT", "Certificat de scolarité"),
        ("ATTESTATION", "Attestation d'inscription"),
        ("RECU", "Reçu de paiement"),
        ("AUTRE", "Autre"),
    )

    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE
    )

    type_document = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="AUTRE"
    )

    titre = models.CharField(
        max_length=200
    )

    fichier = models.FileField(
        upload_to="documents_administratifs/"
    )

    date_ajout = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.titre} - {self.etudiant}"
    
    
class CompteurMatricule(models.Model):
    
    annee = models.IntegerField(
        unique=True
    )

    dernier_numero = models.IntegerField(
        default=0
    )

    def __str__(self):
        return str(self.annee)
    
class ActivationEtudiant(models.Model):
    
    etudiant = models.OneToOneField(
        Etudiant,
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

    def __str__(self):
        return self.etudiant.matricule