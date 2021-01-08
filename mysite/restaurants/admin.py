from django.contrib import admin
from .models import Restaurant, Favourite, Review, MenuItem, Table
from django.utils.safestring import mark_safe
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Resource models for import and export
class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant


class FavouriteResource(resources.ModelResource):
    class Meta:
        model = Favourite


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


class MenuItemResource(resources.ModelResource):
    class Meta:
        model = MenuItem


class TableResource(resources.ModelResource):
    class Meta:
        model = Table


# Custom function for linking tables
def inner_restaurant_link(self, object):
    url = reverse("admin:restaurants_restaurant_change",
                  args=[object.restaurant.id])
    link = '<a href="%s">%s</a>' % (url, object.restaurant.name)
    return mark_safe(link)


# Custom functions for admin-actions
def make_is_cloded_true(restaurantadmin, request, queryset):
    queryset.update(is_closed=True)


def make_is_cloded_false(restaurantadmin, request, queryset):
    queryset.update(is_closed=False)


make_is_cloded_true.short_description = "Make selected restaurants closed"
make_is_cloded_false.short_description = "Make selected restaurants not closed"


def make_currently_free_true(tableadmin, request, queryset):
    queryset.update(currently_free=True)


def make_currently_free_false(tableadmin, request, queryset):
    queryset.update(currently_free=False)


make_currently_free_true.short_description = "Make selected tables as currently free"
make_currently_free_false.short_description = "Make selected tables as currently not free"


# Admin models
class RestaurantAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'address', 'is_closed')
    list_filter = (['is_closed'])
    search_fields = (['name', 'address'])
    actions = [make_is_cloded_true, make_is_cloded_false]
    resource_class = RestaurantResource


class FavouriteAdmin(ImportExportModelAdmin):
    list_display = ('favourite', 'restaurant_link', 'guest')
    list_filter = (['restaurant__name', 'guest__user__username'])
    resource_class = FavouriteResource
    search_fields = (
        ['restaurant__name', 'guest__user__first_name', 'guest__user__last_name', 'guest__user__username'])

    def favourite(self, favourite):
        return favourite.guest.user.first_name + " " + favourite.guest.user.last_name + " (" + favourite.restaurant.name + ")"

    def restaurant_link(self, favourite):
        return inner_restaurant_link(self, favourite)
    restaurant_link.short_description = 'Restaurant'


class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('guest', 'comment', 'rating', 'restaurant_link', 'posted')
    list_filter = (
        ['restaurant__name', 'guest__user__username', 'rating', 'posted'])
    search_fields = (
        ['restaurant__name', 'guest__user__first_name', 'guest__user__last_name', 'guest__user__username'])
    resource_class = ReviewResource

    def restaurant_link(self, review):
        return inner_restaurant_link(self, review)
    restaurant_link.short_description = 'Restaurant'


class MenuItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'restaurant_link')
    list_filter = (['restaurant__name'])
    search_fields = (['name', 'restaurant__name'])
    resource_class = MenuItemResource

    def restaurant_link(self, menuItem):
        return inner_restaurant_link(self, menuItem)
    restaurant_link.short_description = 'Restaurant'


class TableAdmin(ImportExportModelAdmin):
    list_display = ('number', 'restaurant_link', 'currently_free')
    list_filter = (['restaurant', 'currently_free'])
    search_fields = (['restaurant__name'])
    actions = [make_currently_free_true, make_currently_free_false]
    resource_class = TableResource

    def restaurant_link(self, table):
        return inner_restaurant_link(self, table)
    restaurant_link.short_description = 'Restaurant'


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Table, TableAdmin)
