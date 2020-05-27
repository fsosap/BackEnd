from django.shortcuts import render
from rest_framework import viewsets
from .models import Temperature
from .serializers import TemperatureSerializer

class TemperaturesViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('-created')
    serializer_class = TemperatureSerializer