from __future__ import unicode_literals

from django.db import models

class Orden(models.Model):
    cantidad = models.IntegerField()
    producto = models.CharField(max_length=30)
    mesa = models.IntegerField()
