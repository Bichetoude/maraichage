# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('remarque', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Envahisseurs',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('remarque', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Espece',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('faculte_germinative', models.IntegerField(blank=True, null=True, verbose_name='faculte germinative en année')),
                ('temps_levee', models.IntegerField(blank=True, null=True, verbose_name='Temps de levée en jour')),
                ('amendement_type', models.CharField(blank=True, max_length=200, null=True)),
                ('amendement_qualite', models.CharField(blank=True, max_length=200, null=True)),
                ('amendement_quantite', models.IntegerField(blank=True, null=True)),
                ('remarque', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lutte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('moyen_de_lutte', models.TextField(blank=True, null=True)),
                ('envahisseurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.Envahisseurs')),
            ],
        ),
        migrations.CreateModel(
            name='Realistation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_min', models.DateField()),
                ('date_max', models.DateField(blank=True, null=True)),
                ('regularite_jour', models.IntegerField(blank=True, null=True)),
                ('saisonnalité', models.CharField(blank=True, max_length=200, null=True)),
                ('remarque', models.TextField(blank=True, null=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.Action')),
            ],
        ),
        migrations.CreateModel(
            name='SituationGEO',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('remarque', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCulture',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduction',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('remarque', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variete',
            fields=[
                ('nom', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('remarque', models.TextField(blank=True, null=True)),
                ('actions', models.ManyToManyField(to='base_connaissances.Action')),
                ('envahisseurs', models.ManyToManyField(through='base_connaissances.Lutte', to='base_connaissances.Envahisseurs')),
                ('espece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.Espece')),
                ('situations_geo', models.ManyToManyField(to='base_connaissances.SituationGEO')),
                ('types_production', models.ManyToManyField(to='base_connaissances.TypeProduction')),
            ],
        ),
        migrations.AddField(
            model_name='realistation',
            name='situation_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.SituationGEO'),
        ),
        migrations.AddField(
            model_name='realistation',
            name='type_production',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.TypeProduction'),
        ),
        migrations.AddField(
            model_name='realistation',
            name='variete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.Variete'),
        ),
        migrations.AddField(
            model_name='lutte',
            name='variete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.Variete'),
        ),
        migrations.AddField(
            model_name='espece',
            name='type_culture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_connaissances.TypeCulture'),
        ),
        migrations.AlterUniqueTogether(
            name='realistation',
            unique_together=set([('variete', 'action', 'type_production', 'situation_geo')]),
        ),
    ]