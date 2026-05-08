from django.shortcuts import render

from rest_framework import viewsets
from .models import Driver, Car, Fine
from .serializers import (
    DriverWithCarsSerializer, DriverWritableSerializer,
    CarWithFinesSerializer, CarWritableSerializer,
    FineSerializer
)


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.prefetch_related('cars__fines').all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DriverWritableSerializer
        return DriverWithCarsSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.prefetch_related('fines').all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CarWritableSerializer
        return CarWithFinesSerializer


class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer