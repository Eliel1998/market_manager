# Generated by Django 4.2.13 on 2024-09-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]
