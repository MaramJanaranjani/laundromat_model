from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length = 10, null = True, blank = True, default = None)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class laundries(models.Model):
    laundry_name = models.CharField(max_length = 20)
    city_areamapid = models.CharField(max_length = 10)
    sector_id = models.CharField(max_length = 10)
    phone_no = models.IntegerField(default=10)
    def __str__(self):
            return self.name

