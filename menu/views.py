from django.shortcuts import render
from rest_framework import generics
from .models import Pizza
from .serializers import PizzaSerializer # type: ignore

class PizzaListCreate(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

