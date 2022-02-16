from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField()
  icon_image_url = models.URLField(max_length=300)
  date_created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['id']
    
  def get_absolute_url(self):
    return f'{self.slug}'
    
  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  price = models.DecimalField(max_digits=7, decimal_places=2)
  description = models.TextField(max_length=200, blank=True, null=True)
  product_image = models.ImageField(upload_to='uploads/')
  date_created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_created']
    
  def get_absolute_url(self):
    return f"/{self.category.slug}/{self.name}/"
    
  def category_slug(self):
    return self.category.slug
    
  def img_path(self):
    return 'http://127.0.0.1:8000' + self.product_image.url
    
  def __str__(self):
    return self.name
