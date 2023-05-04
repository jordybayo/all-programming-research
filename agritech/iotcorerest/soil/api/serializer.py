from rest_framework import serializers
from soil.models import SoilValues


class SoilValuesSerializer(serializers.Serializer):
    class Meta:
        model  = SoilValues
        fields = ['soil_moisture', 'soil_temp', 'soild_ph']
