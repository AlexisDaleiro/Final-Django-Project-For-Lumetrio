from rest_framework.routers import DefaultRouter
from api1.views import  MarketApiViewSet
from rest_framework import routers
from django.urls import path, include

market_router = routers.DefaultRouter()

market_router.register('market', MarketApiViewSet)

urlpatterns = [
    path('', include(market_router.urls)),
    
]
# path('', include(market_router.urls)),
# # path('market/create/', MarketApiViewSet.as_view({'market': 'create'}), name='market-create'),