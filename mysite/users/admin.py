from django.contrib import admin

# Register your models here.
from .models import Guest, Manager

admin.site.register(Guest)
admin.site.register(Manager)
