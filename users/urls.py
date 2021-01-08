from . import views
from django.urls import path
from rest_framework import routers
from .api import GuestViewSet, ManagerViewSet

router = routers.DefaultRouter()
router.register('api/guests', GuestViewSet, 'guests')
router.register('api/managers', ManagerViewSet, 'managers')

urlpatterns = router.urls
