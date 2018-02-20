from django.db import models

class Famille(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.nom


class Espece(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200, null=False, unique=True)
    id_famille = models.ForeignKey('Famille')
    nom_latin_genre = models.CharField(max_length=200)
    nom_latin_espece = models.CharField(max_length=200)
    faculte_germinative = models.IntegerField(null=True, verbose_name="Faculté germinative en années")
    temps_levee = models.IntegerField(null=True, verbose_name="Temps de levée en jours")
    description = models.TextField(blank=True, null=True)
    gen_periode_recolte = models.BooleanField(default=False)
    gen_periode_semis = models.BooleanField(default=False)
    gen_forme = models.BooleanField(default=False)
    gen_conservation = models.BooleanField(default=False)
    gen_vitesse_croissance = models.BooleanField(default=False)
    gen_utilisation_culinaire = models.BooleanField(default=False)
    image_espece = models.ImageField(blank=True)

    def __str__(self):
        return self.nom


class VarieteGenerique(models.Model):
    id = models.AutoField(primary_key=True)
    id_espece = models.ForeignKey('Espece')
    nom = models.CharField(max_length=200, null=False)
    remarque = models.TextField(blank=True, null=True)
    periode_recolte = models.CharField(max_length=200,blank=True)
    periode_semis = models.CharField(max_length=200,blank=True)
    forme = models.CharField(max_length=200,blank=True)
    conservation = models.CharField(max_length=200,blank=True)
    vitesse_croissance = models.CharField(max_length=200,blank=True)
    utilisation_culinaire = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.nom

    class Meta:
       unique_together = ("id_espece", "nom")

class Variete(models.Model):
    id = models.AutoField(primary_key=True)
    id_variete_generique = models.ForeignKey('VarieteGenerique')
    nom = models.CharField(max_length=200, null=False)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Ravageur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Lutte(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class PbCulture(models.Model):
    id = models.AutoField(primary_key=True)
    id_ravageur = models.ForeignKey('Ravageur')
    id_espece = models.ForeignKey('Espece')
    id_lutte = models.ManyToManyField('Lutte')
    description = models.TextField(blank=True, null=True)
    image_pb_culture = models.ImageField(blank=True)


    def __str__(self):
        return self.nom


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Pratique(models.Model):
    id = models.AutoField(primary_key=True)
    id_espece = models.ForeignKey('Espece')
    id_action = models.ForeignKey('Action')

    def __str__(self):
        return self.nom


class ModalitePratique(models.Model):
    id = models.AutoField(primary_key=True)
    id_pratique = models.ForeignKey('Pratique')
    n_variante = models.IntegerField(null=True)
    id_variete_generique = models.ManyToManyField('VarieteGenerique')
    nom_modalite = models.CharField(max_length=200)
    valeur_modalite = models.CharField(max_length=200)
    image_pratique = models.ImageField(blank=True)

    def __str__(self):
        return self.nom


class PlantesAmies(models.Model):
    id_espece1 = models.OneToOneField('Espece')
    id_espece2 = models.ForeignKey('PlantesAmies2')
    type_relation = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class PlantesAmies2(models.Model):
    id_espece2 = models.OneToOneField('Espece')

    def __str__(self):
        return self.id_espece2.nom


class ZoneGEO(models.Model):
    modificateur_printemps = models.IntegerField(null=True)
    modificateur_automne = models.IntegerField(null=True)
    modificateur_croissance = models.IntegerField(null=True)
