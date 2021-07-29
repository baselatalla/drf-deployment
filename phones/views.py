from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Phone
from .serializer import PhoneSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PhoneListView(generics.ListCreateAPIView):    
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()

class PhoneDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)