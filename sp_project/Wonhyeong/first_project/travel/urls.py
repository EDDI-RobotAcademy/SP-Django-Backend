from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel.controller.views import TravelView

router = DefaultRouter()
router.register(r'account', TravelView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TravelView.as_view({'get': 'list'}), name='travel-list'),
    ]
