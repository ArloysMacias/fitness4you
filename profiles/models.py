from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name_profile = models.CharField(max_length=50, null=True, blank=True)
    email_profile = models.EmailField(max_length=254, null=True, blank=True)
    phone_number_profile = models.CharField(max_length=20, null=True, blank=True)
    country_profile = CountryField(blank_label='Country', null=True, blank=True)
    city_profile = models.CharField(max_length=40, null=True, blank=True)
    address_profile = models.CharField(max_length=80, null=True, blank=True)
    postcode_profile = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile when users are saved
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

