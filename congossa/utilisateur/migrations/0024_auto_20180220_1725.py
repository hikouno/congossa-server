# Generated by Django 2.0.1 on 2018-02-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0023_auto_20180219_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='telephone',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='competence',
            field=models.ManyToManyField(to='composantProfil.Competence'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='experience',
            field=models.ManyToManyField(to='composantProfil.Experience'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='niveauEtude',
            field=models.ManyToManyField(to='composantProfil.NiveauEtude'),
        ),
    ]