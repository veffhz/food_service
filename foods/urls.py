from rest_framework.routers import DefaultRouter

from foods.views import ProductViewSet, RecipientViewSet, OrderViewSet

app_name = 'foods'

router = DefaultRouter(trailing_slash=False)

router.register('recipients/?', RecipientViewSet, basename='recipient')
router.register('product-sets/?', ProductViewSet, basename='product')
router.register('orders/?', OrderViewSet, basename='order')

urlpatterns = router.urls
