from django.db import models
from django.utils.text import slugify



class Product(models.Model):
    name = models.CharField(max_length=95)
    image = models.ImageField(upload_to= 'products/')
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(blank= True, null= True)
    category = models.ForeignKey('Category', on_delete= models.CASCADE, blank=True, null = True)
    description = models.TextField()
    stock=  models.PositiveIntegerField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)+str(self.id)

        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=95)

    def __str__(self):
        return self.name
    