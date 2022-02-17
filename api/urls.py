from django.urls import path
from .views import CategoryAPI, AllProductsAPI, CreateProductAPI,ListCategoryProductsAPI, LatestProductsAPI

urlpatterns = [
  path('category/', CategoryAPI.as_view(), name='category_api'),
  path('all-products/', AllProductsAPI.as_view(), name='all_products'),
  path('create-product/', CreateProductAPI.as_view(), name='create_product'),
  path('category/<slug:category_slug>/products/', ListCategoryProductsAPI.as_view(), name='category_products'),
  path('latest-products/', LatestProductsAPI.as_view(), name='vue_response')
]