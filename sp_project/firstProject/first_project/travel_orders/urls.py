from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel_orders.controller.views import TravelOrdersView

router = DefaultRouter()
router.register(r'travel_orders', TravelOrdersView, basename='travel_orders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', TravelOrdersView.as_view({'post': 'createOrders'}), name='travel-order-create'),
    path('read/<int:orderId>', TravelOrdersView.as_view({'post': 'readOrders'}), name='travel-order-read'),
    path('list/', TravelOrdersView.as_view({'post': 'orderList'}), name='travel-order-list')
]