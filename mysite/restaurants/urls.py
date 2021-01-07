from . import views
from django.urls import path
from rest_framework import routers
from .api import RestaurantViewSet, FavouriteViewSet, ReviewViewSet, MenuItemViewSet, TableViewSet

router = routers.DefaultRouter()
router.register('api/restaurants', RestaurantViewSet, 'restaurants')
router.register('api/favourites', FavouriteViewSet, 'favourites')
router.register('api/reviews', ReviewViewSet, 'reviews')
router.register('api/menuitems', MenuItemViewSet, 'menuitems')
router.register('api/tables', TableViewSet, 'tables')

urlpatterns = router.urls
