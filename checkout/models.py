from django.db import models
from django.conf  import settings
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL


class Address(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    country = CountryField()
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    mobail = models.PositiveIntegerField()


    def __str__(self):
        return self.user.username
