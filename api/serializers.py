from rest_framework import serializers
from api.models import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
    'name', 'slug', 'get_absolute_url', 'date_created'
    )