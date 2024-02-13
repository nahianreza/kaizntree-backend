from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    available_stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    tags = models.ManyToManyField(Tag, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
