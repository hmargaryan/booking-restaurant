from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    rows = models.IntegerField(validators=[MinValueValidator(1)])
    columns = models.IntegerField(validators=[MinValueValidator(1)])
    tables = models.IntegerField(validators=[MinValueValidator(1)])
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    guest = models.ForeignKey('users.Guest', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        guest = self.guest.user.get_full_name(
        ) if self.guest.user.get_full_name() else self.guest.user.username
        return self.restaurant.name + " (" + guest + ")"


class Review(models.Model):
    guest = models.ForeignKey('users.Guest', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    posted = models.DateTimeField(
        'posted time', default=timezone.now, blank=True)

    def __str__(self):
        guest = self.guest.user.get_full_name(
        ) if self.guest.user.get_full_name() else self.guest.user.username
        return guest + " posted on " + self.restaurant.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=1)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.restaurant.name + ")"


class Table(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(1)])
    row = models.IntegerField(validators=[MinValueValidator(1)])
    column = models.IntegerField(validators=[MinValueValidator(1)])
    currently_free = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.restaurant) + " " + str(self.number)
