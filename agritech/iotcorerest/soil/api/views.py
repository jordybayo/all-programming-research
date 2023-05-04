from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from soil.models import SoilValues
from soil.api.serializer import SoilValuesSerializer


