from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse


# Register your models here.
from .models import Restaurant, Favourite, Review, MenuItem, Table


def inner_restaurant_link(self, object):
    url = reverse("admin:restaurants_restaurant_change",
                  args=[object.restaurant.id])
    link = '<a href="%s">%s</a>' % (url, object.restaurant.name)
    return mark_safe(link)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address')
    list_filter = (['is_closed'])
    search_fields = (['name', 'address'])


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('favourite', 'restaurant_link', 'guest')
    list_filter = (['restaurant__name', 'guest__user__username'])
    search_fields = (
        ['restaurant__name', 'guest__user__first_name', 'guest__user__last_name', 'guest__user__username'])

    def favourite(self, favourite):
        return favourite.guest.user.first_name + " " + favourite.guest.user.last_name + " (" + favourite.restaurant.name + ")"

    def restaurant_link(self, favourite):
        return inner_restaurant_link(self, favourite)
    restaurant_link.short_description = 'Restaurant'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('guest', 'comment', 'rating', 'restaurant_link', 'posted')
    list_filter = (
        ['restaurant__name', 'guest__user__username', 'rating', 'posted'])
    search_fields = (
        ['restaurant__name', 'guest__user__first_name', 'guest__user__last_name', 'guest__user__username'])

    def restaurant_link(self, review):
        return inner_restaurant_link(self, review)
    restaurant_link.short_description = 'Restaurant'


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'restaurant_link')
    list_filter = (['restaurant__name'])
    search_fields = (['name', 'restaurant__name'])

    def restaurant_link(self, menuItem):
        return inner_restaurant_link(self, menuItem)
    restaurant_link.short_description = 'Restaurant'


class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'restaurant_link', 'currently_free')
    list_filter = (['restaurant', 'currently_free'])
    search_fields = (['restaurant__name'])

    def restaurant_link(self, table):
        return inner_restaurant_link(self, table)
    restaurant_link.short_description = 'Restaurant'


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Table, TableAdmin)
