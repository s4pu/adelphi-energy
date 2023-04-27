from rest_framework import serializers
from .models import State
from collections import OrderedDict


class StateSerializer(serializers.Serializer):
    energy_yield = serializers.IntegerField()
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
        # setattr(instance, "yield", validated_data.get('yield', getattr(instance, "yield")))
        instance.energy_yield = validated_data.get(
            'energy_yield', instance.energy_yield)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super(StateSerializer, self).to_representation(instance)
        request = self.context.get('request')
        if request is None:
            return data
        capacity = request.query_params.get('capacity')
        if capacity is not None:
            adjusted_yield = int(data.get('energy_yield')) * int(capacity)
            data = OrderedDict(
                energy_yield=adjusted_yield, state=data.get('state'))
        # data["yield"] = data.get('energy_yield')
        # del data["energy_yield"]
        return data

# setattr(StateSerializer, 'yield', serializers.IntegerField())
