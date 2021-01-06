from django.contrib import admin

# Register your models here.
from .models import Reservation, ReservedTable, LastVisit

admin.site.register(Reservation)
admin.site.register(ReservedTable)
admin.site.register(LastVisit)
