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
class cities(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class areas(models.Model):
    area = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class city_areamap(models.Model):
    city_id = models.ForeignKey(cities,max_length=50)
    area_id = models.ForeignKey(areas,max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class sectors(models.Model):
    sectors = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class dresses(models.Model):
    dresses = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class services(models.Model):
    service = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class dress_servicemap(models.Model):
    dress_id = models.CharField(max_length=50)
    service_id = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class excess_cost(models.Model):
    laundry_id = models.ForeignKey(laundries,max_length=50)
    days = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class orders(models.Model):
    address = models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    laundry_id = models.ForeignKey(laundries,max_length=50)
    dress_service_map_id = models.ForeignKey(dress_servicemap,max_length=50)
    excess_cost_id = models.ForeignKey(excess_cost,max_length=50)
    user_id = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    def __str__(self):
        return self.name
