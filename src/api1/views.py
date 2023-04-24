from rest_framework.viewsets import ModelViewSet
from api1.serializers import MarketSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics
from marketplace.models import Item

class MarketApiViewSet(ModelViewSet):
    serializer_class = MarketSerializer
    queryset = Item.objects.all()
