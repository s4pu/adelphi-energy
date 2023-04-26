from django.db import models


class State(models.Model):
    energy = models.IntegerField()
    state = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['state']
