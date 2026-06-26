from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email obligatoire")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email,
            password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    TYPES = (
        ("ADMIN", "Administrateur"),
        ("ENSEIGNANT", "Enseignant"),
        ("ETUDIANT", "Etudiant"),
    )

    email = models.EmailField(unique=True)

    nom = models.CharField(max_length=100)

    prenom = models.CharField(max_length=100)

    telephone = models.CharField(
        max_length=20,
        blank=True
    )

    photo = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    type_utilisateur = models.CharField(
        max_length=20,
        choices=TYPES
    )

    is_active = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Notification(models.Model):
    """
    Notifications génériques envoyées à un utilisateur
    (étudiant, enseignant ou admin) : absence signalée,
    paiement en attente, nouvelle note disponible, etc.
    """

    TYPE_CHOICES = (
        ("ABSENCE", "Absence"),
        ("PAIEMENT", "Paiement"),
        ("NOTE", "Note"),
        ("ANNONCE", "Annonce"),
        ("INFO", "Information"),
    )

    destinataire = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    type_notification = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="INFO"
    )

    titre = models.CharField(
        max_length=150
    )

    message = models.TextField()

    lu = models.BooleanField(
        default=False
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.titre} - {self.destinataire}"