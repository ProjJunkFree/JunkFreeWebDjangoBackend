from django.db import models
from django.conf import settings

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
        ('appliances', 'Appliances'),
        ('books', 'Books'),
        ('other', 'Other'),
    ])
    condition = models.CharField(max_length=50, choices=[
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('used', 'Used'),
    ])
    image = models.ImageField(upload_to='junk', blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reserved_items', null=True, blank=True)