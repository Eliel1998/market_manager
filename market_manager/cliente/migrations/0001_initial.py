# Generated by Django 4.2.13 on 2024-09-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
