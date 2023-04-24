from rest_framework.routers import DefaultRouter
from api.views import PostApiViewSet
from rest_framework import routers
from django.urls import path, include

router_posts = DefaultRouter()

router_posts.register('posts', PostApiViewSet)

urlpatterns = [
    path('', include(router_posts.urls)),
]