from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from energy.models import State
from energy.serializers import StateSerializer


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


def state_detail(request, pk):
    """
    Retrieve, update or delete a code state.
    """
    try:
        state = State.objects.get(pk=pk)
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
