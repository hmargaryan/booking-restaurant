from django.contrib import admin

# Register your models here.
from .models import Restaurant, Favourite, Review, MenuItem, Table

admin.site.register(Restaurant)
admin.site.register(Favourite)
admin.site.register(Review)
admin.site.register(MenuItem)
admin.site.register(Table)
