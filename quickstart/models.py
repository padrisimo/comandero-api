from __future__ import unicode_literals

from django.db import models

class Orden(models.Model):
    mesa = models.IntegerField()

    def lines(self):
        return self.line_set.all()


class Line(models.Model):
    cantidad = models.IntegerField()
    producto = models.CharField(max_length=30)
    orden = models.ForeignKey(Orden, related_name='lines', on_delete=models.CASCADE)

