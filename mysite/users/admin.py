from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
from .models import Guest, Manager


class GuestAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')
    list_filter = (['country'])
    search_fields = (
        ['user__username', 'user__first_name', 'user__last_name'])


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant_link')
    list_filter = (['restaurant__name'])
    search_fields = (
        ['user__username', 'user__first_name', 'user__last_name'])

    def restaurant_link(self, manager):
        url = reverse("admin:restaurants_restaurant_change",
                      args=[manager.restaurant.id])
        link = '<a href="%s">%s</a>' % (url, manager.restaurant.name)
        return mark_safe(link)
    restaurant_link.short_description = 'Restaurant'


admin.site.register(Guest, GuestAdmin)
admin.site.register(Manager, ManagerAdmin)
