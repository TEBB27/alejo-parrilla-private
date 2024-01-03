from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .serializers import menuSerializer, bookingSerializer, contactSerializer, recomendationSerializer
from .models import menu, contact, booking, recomendation
# Create your views here.

class menuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
    def create(self, request):
        name = request.data['name']
        try:
            menu.objects.get(name = name)
            return Response({'message': 'El producto ya existe en la base de datos'})
        except ObjectDoesNotExist:
            menu_item = menu(name=name)
            menu_item.save()
            return Response({'message': 'El producto se ha registrado satisfactoriamente'})
    

class contactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contactSerializer
    
    def create(self, request):
        email = request.data['email']
        try:
            contact.objects.get(email=email)
            return Response({'message': 'El correo ya existe en la base de datos'})
        except ObjectDoesNotExist:
            client = contact(email=email)
            client.save()
            return Response({'message': 'El correo se ha registrado satisfactoriamente'})
        
    def update(self, request, *args, **kwargs):
        email = request.data['email']
        if contact.objects.filter(email=email).exclude(pk=kwargs['pk']).exists():
            return Response({'message': 'El correo ya existe en la base de datos'}, status=400)
        return super().update(request, *args, **kwargs)
    
class bookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    
class recomendationViewSet(viewsets.ModelViewSet):
    queryset = recomendation.objects.all()
    serializer_class = recomendationSerializer
    
class menuListByCategory(generics.ListAPIView):
    serializer_class = menuSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return menu.objects.filter(category=category)