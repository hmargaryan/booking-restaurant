from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        'restaurants.Restaurant', on_delete=models.CASCADE)

    def __str__(self):
        user = self.user.get_full_name() if self.user.get_full_name() else self.user.username
        return user + " (" + self.restaurant.name + ")"
