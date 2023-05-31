import datetime

from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nom}\n{self.descriptif}\n\n"
        return chaine

class Produits(models.Model):
    nom = models.CharField(max_length=100)
    date_peremption = models.DateField(blank=True, null = True)
    marques = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.nom} de la marque {self.marques} est un {self.categorie}"
        return chaine

class Clients(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription=models.DateField()
    adresse = models.TextField(null = False, blank = False)

    def __str__(self):
        return f"{self.prenom} {self.nom} s'est inscrit le {self.date_inscription} et habite au {self.adresse}."

class Commandes(models.Model):
    date_commande=models.DateField()
    client_id=models.ForeignKey("client", on_delete=models.CASCADE)

    def __str__(self):
        return f"Cette commande a ete placée le {self.date_commande} par {self.client_id}."
