from django.db import models


class State(models.Model):
    val = models.IntegerField()
    state = models.CharField(max_length=64)

    def __str__(self):
        return self.state
