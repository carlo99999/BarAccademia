from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Prodotto(models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome

class Ordine(models.Model):
    data = models.DateField()
    cliente = models.CharField(max_length=100)
    prodotto = models.CharField(max_length=200)
    n_scontrino = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.data} - {self.cliente} - {self.prodotto} - {self.n_scontrino}'
    

    