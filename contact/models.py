from django.db import models

# Create your models here.


class Conatct(models.Model):
    name  = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()


    def __str__(self):
        return self.email