from django.db import models

# Create your models here.

# Table des enfants
class Enfant(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    allergies = models.TextField(blank=True, default='')
    nom_prefere = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

# Table des activités (cantine, accueil matin, etc.)
class Activite(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    telephone_contact = models.CharField(max_length=20, blank=True, default='')
    test = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
    
# Table des inscriptions (qui va où)
class Inscription(models.Model):
    enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    date = models.DateField()
    statut = models.CharField(max_length=20, choices=[
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('attente', 'En attente'),
    ], default='confirme')

    def __str__(self):
        return f"{self.enfant} → {self.activite} ({self.date})"