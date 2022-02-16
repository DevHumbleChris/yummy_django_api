from rest_framework import serializers
from api.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
    'id', 'name', 'slug', 'icon_image_url', 'get_absolute_url', 'date_created',
    )

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id', 'category', 'name', 'slug', 'price', 'description', 'product_image', 'category_slug', 'get_absolute_url', 'date_created',
    )
