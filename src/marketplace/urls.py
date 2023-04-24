from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, MarketCommunicationCreateView

app_name = 'market'

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('<int:pk>/communication/', MarketCommunicationCreateView.as_view(), name='communication-create'),
]
