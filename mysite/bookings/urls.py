from . import views
from django.urls import path
from rest_framework import routers
from .api import ReservationViewSet, ReservedTableViewSet, LastVisitViewSet

router = routers.DefaultRouter()
router.register('api/reservations', ReservationViewSet, 'reservations')
router.register('api/reservedtables', ReservedTableViewSet, 'reservedtables')
router.register('api/lastvisits', LastVisitViewSet, 'lastvisits')

urlpatterns = router.urls
