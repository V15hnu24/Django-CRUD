from rest_framework import serializers
from firstapp.models import Location, Item, TodoItem

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
