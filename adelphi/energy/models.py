from django.db import models
from django.db.models.signals import class_prepared
from jsonfield import JSONField


class State(models.Model):
    energy_yield = models.IntegerField()
    state = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['state']


# setattr(State, 'yield', models.IntegerField())


# def add_field(sender, **kwargs):
#     if sender.__name__ == "State":
#         field = JSONField('yield')
#         field.contribute_to_class(sender, 'yield')


# class_prepared.connect(add_field)
