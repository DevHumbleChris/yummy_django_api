from django.contrib import admin
from api.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Category Name', {'fields': ['name']}),
    ('Category Slug', {'fields': ['slug']}),
    ('Category Icon Image URL', {'fields': ['icon_image_url']})
  ]
  
class ProductAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Product Information', {'fields': ['category', 'name', 'slug', 'price', 'description']}), 
    ('Product Image', {'fields': ['product_image']})
  ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)