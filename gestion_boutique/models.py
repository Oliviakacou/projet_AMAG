from django.db import models

# Create your models here.

class Arrivage_Chaussure(models.Model):
    id_arrivage = models.BigIntegerField(primary_key=True)
    date_arrivage = models.DateField()
    description_ch_arrivage = models.TextField()
    pointure_min_arrivage = models.IntegerField()
    pointure_max_arrivage = models.IntegerField()
    quantite_arrivage = models.IntegerField()
    prix_unitaire_achat = models.DecimalField(max_digits=10, decimal_places=2)
    total_arrivage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Arrivage {self.id_arrivage} - {self.description_ch_arrivage}'
    
class Client(models.Model):
    id_client = models.BigIntegerField(primary_key=True)
    date_passage_client = models.DateField(null=True, blank=True)
    nom_client = models.CharField(max_length=10)
    prenom_client = models.CharField(max_length=10)
    numero_client = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)
    adresse_client = models.CharField(max_length=10)
    remarque_achat = models.CharField(max_length=15, blank=True)

def __str__(self):
        return f'Client {self.nom_client} {self.prenom_client}'


# Table vente
class Vente(models.Model):
    id_vente = models.BigIntegerField(primary_key=True)
    date_vente = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description_chaussure = models.CharField(max_length=30)
    pointure_chaussure = models.DecimalField(max_digits=5, decimal_places=2)
    quantite_vendue = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Vente {self.id_vente} - Client {self.client}'

