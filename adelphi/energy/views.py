from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from energy.models import State
from energy.serializers import StateSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F


class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state']

    def get_queryset(self):
        """
        Optionally restricts the returned states to a given state name,
        by filtering against the `state` query parameter in the URL.
        """
        statename = self.request.query_params.get('state')
        capacity = self.request.query_params.get('capacity')
        if statename is not None:
            queryset = State.objects.filter(state=statename)
        else:
            queryset = State.objects.all()
        # if capacity is not None:

            # print(1)
            # def update_queryset(datum):
            #     return {"energy_yield": datum.energy_yield * capacity, "state": datum.state}
            # print(2)
            # mapiterator = (update_queryset, queryset)
            # print(3)
            # new_queryset = set(mapiterator)
            # print(new_queryset)

            # new_queryset = []
            # for d in queryset:
            #     new_yield = d.energy_yield * capacity
            #     new_d = {"energy_yield": new_yield, "state": d.state}
            #     new_queryset.append(new_d)
            #     return JsonResponse(new_d, safe=False)  # hier dann yield??
        return queryset


def state_list(request):
    """
    List all code state, or create a new state.
    """
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def state_detail(request, input):
    """
    Retrieve, update or delete a code state.
    """
    try:
        state = State.objects.get(state=input)
    except State.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StateSerializer(state, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        state.delete()
        return HttpResponse(status=204)
