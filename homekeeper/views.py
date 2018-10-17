from django.shortcuts import render
from rest_framework import viewsets
from homekeeper.models import Homekeeper
from homekeeper.serializers import HomekeeperSerializer

class HomeKeeperViewSet(viewsets.ModelViewSet):
    queryset = Homekeeper.objects.all()
    serializer_class = HomekeeperSerializer
