# Generated by Django 4.2.13 on 2024-09-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preco'),
        ),
    ]
