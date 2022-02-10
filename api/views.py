from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from api.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CategoryAPI(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  
  def get(self, request, *args, **kwargs):
    return self.list(self, request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(self, request, *args, **kwargs)

class LatestProductsAPI(mixins.ListModelMixin, generics.GenericAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  def get(self, request, *args, **kwargs):
    return self.list(self, request, *args, **kwargs)

class CreateProductAPI(mixins.CreateModelMixin, generics.GenericAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  
  def post(self, request, *args, **kwargs):
    return self.create(self, request, *args, **kwargs)

class ListCategoryProductsAPI(APIView):
  def get(self, request, category_name, *args, **kwargs):
    qs = Product.objects.filter(category=category_name)
    serializer = ProductSerializer(qs, many=True)
    return Response(serializer.data)

class VueApiResponse(APIView):
  def post (self, vue_data, *args, **kwarg):
    print(vue_data)
    return Response(vue_data)