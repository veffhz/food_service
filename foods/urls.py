from rest_framework.routers import DefaultRouter

from foods.views import ProductViewSet, RecipientViewSet

app_name = 'foods'

router = DefaultRouter()

router.register('recipients', RecipientViewSet, basename='recipient')
router.register('product-sets', ProductViewSet, basename='product')

urlpatterns = router.urls
