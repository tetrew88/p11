# Generated by Django 3.1.3 on 2021-01-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('substitutesearch', '0001_initial'),
        ('favorites', '0003_remove_favorites_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='substitutesearch.product'),
        ),
    ]