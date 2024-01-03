from rest_framework import serializers
from .models import menu, contact, recomendation, booking

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'

class recomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = recomendation
        fields = '__all__'