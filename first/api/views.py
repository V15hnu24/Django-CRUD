from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from firstapp.models import Location, Item, TodoItem
from .serializers import LocationSerializer

@api_view(['GET'])
def getLocations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addLocation(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLocation(request, pk):
    try:
        location = Location.objects.get(id=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    location.delete()
    return Response("Location deleted")

@api_view(['PUT'])
def updateLocation(request, pk):
    try:
        location = Location.objects.get(id=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = LocationSerializer(instance=location, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
