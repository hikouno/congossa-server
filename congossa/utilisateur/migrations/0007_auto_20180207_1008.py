# Generated by Django 2.0.1 on 2018-02-07 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0006_auto_20180207_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='prenom',
        ),
    ]