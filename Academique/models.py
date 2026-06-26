from django.db import models


class Cours(models.Model):

    SEMESTRES = (
        (1, "Semestre 1"),
        (2, "Semestre 2"),
    )

    code = models.CharField(max_length=20)

    nom = models.CharField(max_length=150)

    responsable = models.ForeignKey(
    "Enseignant.Enseignant",
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)

    classe = models.ForeignKey(
        "Admin.Classe",
        on_delete=models.CASCADE
    )

    semestre = models.IntegerField(
        choices=SEMESTRES
    )

    credit = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.nom}"


class Seance(models.Model):

    cours = models.ForeignKey(
        Cours,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    heure_debut = models.TimeField()

    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.cours.nom} - {self.date}"


class Evaluation(models.Model):

    TYPE_CHOICES = (
        ('CC', 'CC'),
        ('TP', 'TP'),
        ('EXAM', 'EXAM')
    )

    cours = models.ForeignKey(
        Cours,
        on_delete=models.CASCADE
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    titre = models.CharField(
        max_length=100
    )

    coefficient = models.FloatField()

    date_evaluation = models.DateField()

    publie = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.cours.nom} - {self.type}"


class Note(models.Model):

    etudiant = models.ForeignKey(
        "app.Etudiant",
        on_delete=models.CASCADE
    )

    evaluation = models.ForeignKey(
        Evaluation,
        on_delete=models.CASCADE
    )

    note = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    appreciation = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = (
            "etudiant",
            "evaluation"
        )

    def __str__(self):
        return f"{self.etudiant} - {self.note}"


class Presence(models.Model):

    STATUS = (
        ('PRESENT', 'Présent'),
        ('ABSENT', 'Absent'),
    )

    seance = models.ForeignKey(
        Seance,
        on_delete=models.CASCADE
    )

    etudiant = models.ForeignKey(
        "app.Etudiant",
        on_delete=models.CASCADE
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUS
    )

    class Meta:
        unique_together = (
            "seance",
            "etudiant"
        )

    def __str__(self):
        return f"{self.etudiant} - {self.statut}"