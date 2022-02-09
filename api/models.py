from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField()
  date_created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_created']
    
  def get_absolute_url(self):
    return '/{}/'.self.slug
