from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Miejscowosc(models.Model):
    nazwa_miejscowosci = models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa_miejscowosci


class Druzyna(models.Model):
    nazwa_druzyny = models.CharField(max_length=200)
    adres_klubu = models.CharField(max_length=200)
    aktualna_liga = models.CharField(max_length=200)
    id_miejscowosc = models.ForeignKey(Miejscowosc, on_delete = models.CASCADE)
    def __str__(self):
        return self.nazwa_druzyny

class Pilkarz(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    data_urodzenia = models.DateTimeField(
            blank=True, null=True)
    id_druzyna = models.ForeignKey(Druzyna, on_delete = models.CASCADE)

    def __str__(self):
        return self.imie + self.nazwisko


class Mecz(models.Model):
    data_rozegrania = models.DateTimeField(
            blank=True, null=True)
    nazwa_meczu = models.CharField(max_length=200)
    druzyna_gosci = models.ForeignKey(Druzyna,on_delete = models.CASCADE, related_name='druzyna_goscii')
    druzyna_gospodarzy = models.ForeignKey(Druzyna, on_delete = models.CASCADE, related_name='druzyna_gospodarzyy')
    wynik_goscia = models.IntegerField(default=0)
    wynik_gospodarza = models.IntegerField(default=0)
    id_miejscowosci = models.ForeignKey(Miejscowosc, on_delete=models.CASCADE)
    def __str__(self):
        return self.nazwa_meczu


class Granie(models.Model):
    id_pilkarza = models.ForeignKey(Pilkarz, on_delete = models.CASCADE)
    statystki_mecz = models.CharField(max_length=200)
    id_meczu = models.ForeignKey(Mecz, on_delete = models.CASCADE)
    pozycja = models.CharField(max_length=200)
    liczba_strzelonych_bramek = models.IntegerField(default=0)
    minuta_czerwnoej_kartki = models.IntegerField(default=0)

    def __str__(self):
        return self.statystki_mecz
