from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel_orders.controller.views import TravelOrdersView

router = DefaultRouter()
router.register(r'travel_orders', TravelOrdersView, basename='travel_orders')

urlpatterns = [
    path('', include(router.urls)),
]