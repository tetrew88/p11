# Generated by Django 3.0.6 on 2020-10-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
        ('authentification', '0002_auto_20200823_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='favorites.Favorites'),
        ),
    ]
