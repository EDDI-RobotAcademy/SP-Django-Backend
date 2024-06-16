from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel_board.controller.views import (TravelBoardView)

router = DefaultRouter()
router.register(r'travelBoard', TravelBoardView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TravelBoardView.as_view({'get': 'list'}), name='travel-board-list'),
    path('register', TravelBoardView.as_view({'post': 'create'}), name='travel-board-register'),
]