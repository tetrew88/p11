# Generated by Django 3.0.6 on 2020-08-23 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('substitutesearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mailAdress', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('favorites', models.ManyToManyField(related_name='product', to='substitutesearch.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
