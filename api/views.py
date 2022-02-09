from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from api.models import Category
from .serializers import CategorySerializer

class CategoryAPI(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  
  def get(self, request, *args, **kwargs):
    return self.list(self, request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(self, request, *args, **kwargs)
