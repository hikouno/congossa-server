# Generated by Django 2.0.1 on 2018-02-14 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offre', '0010_offre_experiencerequise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='metier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='composantProfil.Metier'),
        ),
    ]
