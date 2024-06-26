from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Programmer_serializer
from .models import Programmer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = Programmer_serializer