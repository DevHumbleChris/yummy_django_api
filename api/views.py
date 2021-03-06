from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from api.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CategoryAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  
  def get(self, request, *args, **kwargs):
    return self.list(self, request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class AllProductsAPI(mixins.ListModelMixin, generics.GenericAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  def get(self, request, *args, **kwargs):
    return self.list(self, request, *args, **kwargs)
    
class LatestProductsAPI(mixins.ListModelMixin, generics.GenericAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()[:5]
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

class CreateProductAPI(mixins.CreateModelMixin, generics.GenericAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class ListCategoryProductsAPI(APIView):
  def get(self, request, category_slug, *args, **kwargs):
    print(category_slug)
    qs = Product.objects.filter(category__slug= category_slug)
    serializer = ProductSerializer(qs, many=True)
    return Response(serializer.data)

class VueApiResponse(APIView):
  def post (self, vue_data, *args, **kwarg):
    print(vue_data)
    return Response(vue_data)