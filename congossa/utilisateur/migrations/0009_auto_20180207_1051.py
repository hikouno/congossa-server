# Generated by Django 2.0.1 on 2018-02-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0008_auto_20180207_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='competencePossede',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='dateDeNaissance',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='diplomePossede',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='formationPossede',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='localisation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
