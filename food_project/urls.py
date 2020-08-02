from django.urls import path, include
from rest_framework.routers import DefaultRouter

from foods.views import product_sets, product_detail, RecipientViewSet

router = DefaultRouter()

router.register('api/recipients', RecipientViewSet, basename='recipient')

urlpatterns = [
    path('', include(router.urls)),

    path('api/product-sets/', product_sets, name='product-sets'),
    path('api/product-sets/<int:pk>/', product_detail, name='product-detail'),
]
