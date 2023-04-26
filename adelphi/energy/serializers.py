from rest_framework import serializers
from .models import State


class StateSerializer(serializers.Serializer):
    # energy = serializers.IntegerField()
    state = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `State` instance, given the validated data.
        """
        return State.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `State` instance, given the validated data.
        """
        setattr(instance, "yield", validated_data.get(
            'yield', getattr(instance, "yield")))
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance


setattr(StateSerializer, 'yield', serializers.IntegerField())
