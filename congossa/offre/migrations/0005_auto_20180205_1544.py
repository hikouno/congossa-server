# Generated by Django 2.0.1 on 2018-02-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offre', '0004_auto_20180205_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='dateDebut',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='offre',
            name='dateDebut',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='offre',
            name='dureeContrat',
            field=models.CharField(max_length=200),
        ),
    ]