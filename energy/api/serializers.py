from django.contrib.auth.models import User, Group
from rest_framework import serializers


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group  # User
        fields = ['val', 'state']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # model = Group
#         fields = ['url', 'name']
