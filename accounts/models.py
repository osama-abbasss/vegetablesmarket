from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/')
    address = models.CharField(max_length=124)
    terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])
        profile.save()


post_save.connect(create_profile, sender=User)
