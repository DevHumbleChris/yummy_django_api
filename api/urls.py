from django.urls import path
from .views import CategoryAPI, LatestProductsAPI, CreateProductAPI,ListCategoryProductsAPI, VueApiResponse

urlpatterns = [
  path('category/', CategoryAPI.as_view(), name='category_api'),
  path('all-products/', LatestProductsAPI.as_view(), name='latest_products'),
  path('create-product/', CreateProductAPI.as_view(), name='create_product'),
  path('category/<str:category_name>/products/', ListCategoryProductsAPI.as_view(), name='category_products'),
  path('vue-response/', VueApiResponse.as_view(), name='vue_response')
]