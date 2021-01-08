from django.contrib import admin
from .models import Guest, Manager
from django.utils.safestring import mark_safe
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Resource models for import and export
class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest


class ManagerResource(resources.ModelResource):
    class Meta:
        model = Manager


# Admin models
class GuestAdmin(ImportExportModelAdmin):
    list_display = ('user', 'country')
    list_filter = (['country'])
    search_fields = (
        ['user__username', 'user__first_name', 'user__last_name'])
    resource_class = GuestResource


class ManagerAdmin(ImportExportModelAdmin):
    list_display = ('user', 'restaurant_link')
    list_filter = (['restaurant__name'])
    search_fields = (
        ['user__username', 'user__first_name', 'user__last_name'])
    resource_class = ManagerResource

    def restaurant_link(self, manager):
        url = reverse("admin:restaurants_restaurant_change",
                      args=[manager.restaurant.id])
        link = '<a href="%s">%s</a>' % (url, manager.restaurant.name)
        return mark_safe(link)
    restaurant_link.short_description = 'Restaurant'


admin.site.register(Guest, GuestAdmin)
admin.site.register(Manager, ManagerAdmin)
