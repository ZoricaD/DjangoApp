from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Kategorija(models.Model):
    ime = models.CharField(max_length=20)
    opis = models.TextField(max_length=40)
    aktivna = models.BooleanField(default=False)


class Produkt(models.Model):
    ime = models.CharField(max_length=20)
    opis = models.TextField(max_length=40)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    cena = models.IntegerField()
    kolicina = models.IntegerField()


class Klient(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    adresa = models.CharField(max_length=20)
    email = models.EmailField()


class Prodazba(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    kolicina = models.IntegerField()
    datum = models.DateField()
