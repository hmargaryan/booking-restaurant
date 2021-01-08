from django.contrib import admin
from .models import Reservation, ReservedTable, LastVisit
from django.utils.safestring import mark_safe
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Resource models for import and export
class ReservationResource(resources.ModelResource):
    class Meta:
        model = Reservation


class ReservedTableResource(resources.ModelResource):
    class Meta:
        model = ReservedTable


class LastVisitResource(resources.ModelResource):
    class Meta:
        model = LastVisit


# Admin models
class ReservationAdmin(ImportExportModelAdmin):
    list_display = ('reservation', 'restaurant_link',
                    'guest', 'coming', 'duration')
    list_filter = (['restaurant__name', 'guest__user__username', 'coming'])
    search_fields = (['restaurant__name', 'guest__user__username',
                      'guest__user__first_name', 'guest__user__last_name'])
    resource_class = ReservationResource

    def reservation(self, reservation):
        return reservation.restaurant.name + " Reservation"

    def restaurant_link(self, manager):
        url = reverse("admin:restaurants_restaurant_change",
                      args=[manager.restaurant.id])
        link = '<a href="%s">%s</a>' % (url, manager.restaurant.name)
        return mark_safe(link)
    restaurant_link.short_description = 'Restaurant'


class ReservedTableAdmin(ImportExportModelAdmin):
    list_display = ('table', 'reservation')
    search_fields = (['reservation__restaurant__name', 'reservation__guest__user__username',
                      'reservation__guest__user__first_name', 'reservation__guest__user__last_name'])
    resource_class = ReservedTableResource


class LastVisitAdmin(ImportExportModelAdmin):
    list_display = ('reservation', 'guest')
    list_filter = (['guest__user__username'])
    search_fields = (['reservation__restaurant__name', 'guest__user__username',
                      'guest__user__first_name', 'guest__user__last_name'])
    resource_class = LastVisitResource


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservedTable, ReservedTableAdmin)
admin.site.register(LastVisit, LastVisitAdmin)
