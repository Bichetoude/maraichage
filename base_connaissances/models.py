from django.db import models
from django.utils import timezone
from django.db.models import F
from django.db.models.functions import Concat

class TypeCulture(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.nom

class Espece(models.Model):
    type_culture = models.ForeignKey('TypeCulture')
    nom = models.CharField(max_length=200, primary_key=True)
    faculte_germinative = models.IntegerField(blank=True, null=True, verbose_name="faculte germinative en année")
    temps_levee = models.IntegerField(blank=True, null=True, verbose_name="Temps de levée en jour")
    amendement_type = models.CharField(max_length=200, blank=True, null=True)
    amendement_qualite = models.CharField(max_length=200, blank=True, null=True)
    amendement_quantite = models.IntegerField(blank=True, null=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Variete(models.Model):
    espece = models.ForeignKey('Espece')
    nom = models.CharField(max_length=200, primary_key=True)
    remarque = models.TextField(blank=True, null=True)
    actions = models.ManyToManyField('Action')
    situations_geo = models.ManyToManyField('SituationGEO')
    types_production = models.ManyToManyField('TypeProduction')
    envahisseurs = models.ManyToManyField('Envahisseur', through='Lutte')
    #realisation = models.ForeignKey('Realistation')

    def __str__(self):
        return self.nom

class Envahisseur(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class SituationGEO(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class TypeProduction(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Action(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Lutte(models.Model):
    id = models.AutoField(primary_key=True)
    variete = models.ForeignKey('Variete')
    envahisseurs = models.ForeignKey('Envahisseur')
    nom = models.CharField(max_length=200)
    moyen_de_lutte = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Realistation(models.Model):
    variete = models.ForeignKey('Variete')
    action = models.ForeignKey('Action')
    type_production = models.ForeignKey('TypeProduction', blank=True, null=True)
    situation_geo = models.ForeignKey('SituationGEO', blank=True, null=True)
    date_min = models.DateField()
    date_max = models.DateField(blank=True, null=True)
    regularite_jour = models.IntegerField(blank=True, null=True)
    saisonnalité = models.CharField(max_length=200, blank=True, null=True)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.action

    class Meta:
       unique_together = ("variete", "action", "type_production", "situation_geo")
