from django.urls import path

from foods.views import product_sets, product_detail
from foods.views import recipients_list, recipient_detail

urlpatterns = [
    path('recipients/', recipients_list, name='recipients-list'),
    path('recipients/<int:pk>/', recipient_detail, name='recipient-detail'),

    path('product-sets/', product_sets, name='product-sets'),
    path('product-sets/<int:pk>/', product_detail, name='product-detail'),
]
