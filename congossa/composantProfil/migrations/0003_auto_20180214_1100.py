# Generated by Django 2.0.1 on 2018-02-14 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('composantProfil', '0002_auto_20180213_1627'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='diplome',
            new_name='niveauEtude',
        ),
    ]
