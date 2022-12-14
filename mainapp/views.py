from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from mainapp.serializers import(
    Product, ProductSerializer,
    Cart, CartSerializer,
    CartProduct, CartProductSerializer,
)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer



