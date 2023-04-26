# from django.contrib.auth.models import User, Group
from .models import State
from rest_framework import serializers


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['val', 'state']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # model = Group
#         fields = ['url', 'name']
