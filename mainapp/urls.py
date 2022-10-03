from rest_framework.routers import DefaultRouter as DR
from mainapp.views import *


router = DR()
router.register('products', ProductViewSet, basename='product')
router.register('carts', CartViewSet, basename='cart')
router.register('cartproducts', CartProductViewSet, basename='cartproduct')

urlpatterns = []

urlpatterns += router.urls

