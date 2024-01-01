from django.shortcuts import render
from rest_framework import viewsets
from .serializers import menuSerializer, bookingSerializer, contactSerializer, recomendationSerializer
from .models import menu, contact, booking, recomendation
# Create your views here.

class menuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class contactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contactSerializer
    
class bookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    
class recomendationViewSet(viewsets.ModelViewSet):
    queryset = recomendation.objects.all()
    serializer_class = recomendationSerializer