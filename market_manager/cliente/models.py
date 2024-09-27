from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=150)
    email = models.EmailField(verbose_name='Email', blank=False, null=False)