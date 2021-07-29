
from rest_framework import serializers

from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'specifications', 'rating','price', 'company')
        model = Phone