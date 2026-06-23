from django.db import models


class AnneeAcademique(models.Model):

    libelle = models.CharField(max_length=20)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.libelle


class Faculte(models.Model):

    code = models.CharField(max_length=20)

    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Departement(models.Model):

    nom = models.CharField(max_length=150)

    faculte = models.ForeignKey(
        Faculte,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nom


class Filiere(models.Model):

    nom = models.CharField(max_length=150)

    departement = models.ForeignKey(
        Departement,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nom


class Niveau(models.Model):

    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Classe(models.Model):

    nom = models.CharField(max_length=100)

    filiere = models.ForeignKey(
        Filiere,
        on_delete=models.CASCADE
    )

    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.CASCADE
    )

    annee = models.ForeignKey(
        AnneeAcademique,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nom


class Salle(models.Model):

    code = models.CharField(max_length=20)

    capacite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} ({self.capacite} places)"


class Annonce(models.Model):

    enseignant = models.ForeignKey(
        "Enseignant.Enseignant",
        on_delete=models.CASCADE
    )

    titre = models.CharField(max_length=255)

    message = models.TextField()

    fichier = models.FileField(
        upload_to="annonces/",
        blank=True,
        null=True
    )

    classes = models.ManyToManyField(
        Classe
    )

    date_publication = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre


class DocumentCours(models.Model):

    cours = models.ForeignKey(
        "Academique.Cours",
        on_delete=models.CASCADE
    )

    titre = models.CharField(max_length=255)

    fichier = models.FileField(
        upload_to="documents/"
    )

    def __str__(self):
        return self.titre