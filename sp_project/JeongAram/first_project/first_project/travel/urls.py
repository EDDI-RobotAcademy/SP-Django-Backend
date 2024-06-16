from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel.controller.views import TravelView

router = DefaultRouter()
router.register(r'travel', TravelView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TravelView.as_view({'get': 'list'}), name='travel-list'),
    path('register', TravelView.as_view({'post': 'register'}), name='travel-register'),
]