from django.urls import path
from . import views
from .views import AllProductsView, SortedProductsView, EraListView, artifact_detail

urlpatterns = [
    path('', AllProductsView.as_view(), name='products'),
    path('sorted/', SortedProductsView.as_view(), name='sorted_products'),
    path('<str:era>/', EraListView.as_view(), name='era-list'),
    path('artifact/<int:pk>', artifact_detail, name='artifact'),
]
