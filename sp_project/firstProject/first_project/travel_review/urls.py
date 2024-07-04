from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel_review.controller.views import (TravelReviewView)

router = DefaultRouter()
router.register(r'travel_review', TravelReviewView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TravelReviewView.as_view({'get': 'list'}), name='travel-review-list'),
    path('register', TravelReviewView.as_view({'post': 'create'}), name='travel-review-register'),
    path('read/<int:pk>', TravelReviewView.as_view({'get': 'read'}), name='travel-review-read'),
    path('delete/<int:pk>', TravelReviewView.as_view({'delete': 'removeTravelReview'}), name='travel-review-delete'),
    path('modify/<int:pk>', TravelReviewView.as_view({'put': 'modifyTravelReview'}), name='travel-review-modify')
]