from rest_framework import serializers
from api.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
    'name', 'slug', 'get_absolute_url', 'date_created'
    )

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'category', 'name', 'slug', 'price', 'description', 'product_image', 'get_absolute_url', 'date_created'
    )
