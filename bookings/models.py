from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Reservation(models.Model):
    people = models.IntegerField(default=1, validators=[
                                 MinValueValidator(1), MaxValueValidator(50)])
    coming = models.DateTimeField('reservation time')
    duration = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(24)])
    guest = models.ForeignKey('users.Guest', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        'restaurants.Restaurant', on_delete=models.CASCADE)

    def __str__(self):
        person = self.guest.user.get_full_name(
        ) if self.guest.user.get_full_name() else self.guest.user.username
        place = self.restaurant.name
        time = self.coming
        duration = self.duration
        people = self.people
        return person + " in " + place + " at " + str(time) + " for " + str(duration) + " hours with " + str(people - 1) + " person/people"


class ReservedTable(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    table = models.ForeignKey('restaurants.Table', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reservation) + " table: " + str(self.table)


class LastVisit(models.Model):
    tip = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    guest = models.ForeignKey('users.Guest', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reservation) + " for: " + str(self.guest)
