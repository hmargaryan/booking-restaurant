from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
from .models import Reservation, ReservedTable, LastVisit


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'restaurant_link',
                    'guest', 'coming', 'duration')
    list_filter = (['restaurant__name', 'guest__user__username', 'coming'])
    search_fields = (['restaurant__name', 'guest__user__username',
                      'guest__user__first_name', 'guest__user__last_name'])

    def reservation(self, reservation):
        return reservation.restaurant.name + " Reservation"

    def restaurant_link(self, manager):
        url = reverse("admin:restaurants_restaurant_change",
                      args=[manager.restaurant.id])
        link = '<a href="%s">%s</a>' % (url, manager.restaurant.name)
        return mark_safe(link)
    restaurant_link.short_description = 'Restaurant'


class ReservedTableAdmin(admin.ModelAdmin):
    list_display = ('table', 'reservation')
    search_fields = (['reservation__restaurant__name', 'reservation__guest__user__username',
                      'reservation__guest__user__first_name', 'reservation__guest__user__last_name'])


class LastVisitAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'guest')
    list_filter = (['guest__user__username'])
    search_fields = (['reservation__restaurant__name', 'guest__user__username',
                      'guest__user__first_name', 'guest__user__last_name'])


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservedTable, ReservedTableAdmin)
admin.site.register(LastVisit, LastVisitAdmin)
