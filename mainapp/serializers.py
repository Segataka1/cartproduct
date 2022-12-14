from dataclasses import field
from rest_framework import serializers

from mainapp.models import(
    Product, Cart, CartProduct
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'articul')


class CartSerializer(serializers.ModelSerializer):
    products = serializers.ListField(write_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user_name', 'created_at', 'total_price', 'delivery_address',
                  'products',)

        read_only_fields = ('created_at',)

    def create(self, validated_data):
        cart = Cart.objects.create(
            user_name=validated_data.get('user_name'),
            delivery_address=validated_data.get('delivery_address')
        )
        for p in validated_data.get('products'):
            CartProduct.objects.create(
                product=Product.objects.filter(id=p.get('id')).first(),
                cart=cart,
                amount=p.get('amount'),
            )
        cart_price = sum([p.sum_product_price for p in cart.cart_products.all()])
        cart.save()
        return cart
 
    def to_representation(self, instance):
        data = {
            'user_name': instance.user_name,
            'delivery_address': instance.delivery_address,
            'total_price': instance.total_price,
            'created_at': instance.created_at,
            'product': CartProductSerializer(instance=CartProduct.objects.filter)
        }


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'cart', 'total_price', 'amount')
