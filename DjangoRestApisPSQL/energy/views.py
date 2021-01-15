from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Wdmodel
from .serializers import WdmodelSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def energy_list(request):
	# GET list of energy, POST a new energy, DELETE all energy.
	if request.method == 'GET':
		energys = Wdmodel.objects.all()

		title = request.GET.get('title', None)
		if title is not None:
			energys = energys.filter(title__icontains=title)

		energy_serializer = WdmodelSerializer(energys, many=True)
		return JsonResponse(energy_serializer.data, safe=False)
		# 'safe=False' for objects serialization

	elif request.method == 'POST':
		energy_data = JSONParser().parse(request)
		energy_serializer = WdmodelSerializer(data=energy_data)
		if energy_serializer.is_valid():
			energy_serializer.save()
			return JsonResponse(energy_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(energy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		count = Wdmodel.objects.all().delete()
		return JsonResponse({'message': '{} Energys were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def energy_detail(request, pk):
	# find energy by pk (id)
	try:
		energy = Wdmodel.objects.get(pk=pk)
	except Wdmodel.DoesNotExist:
		return JsonResponse({'message': 'The energy does not exist'}, status=status.HTTP_404_NOT_FOUND)

	# GET / PUT / DELETE api
	if request.method == 'GET':
		energy_serializer = WdmodelSerializer(energy)
		return JsonResponse(energy_serializer.data)

	elif request.method == 'PUT':
		energy_data = JSONParser().parse(request)
		energy_serializer = WdmodelSerializer(energy, data=energy_data)
		if energy_serializer.is_valid():
			energy_serializer.save()
			return JsonResponse(energy_serializer.data)
		return JsonResponse(energy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		energy.delete()
		return JsonResponse({'message': 'Energy was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def energy_list_published(request):
	# GET all published energy.
	energys = Wdmodel.objects.filter(published=True)

	if request.method == 'GET':
		energy_serializer = WdmodelSerializer(energys, many=True)
		return JsonResponse(energy_serializer.data, safe=False)