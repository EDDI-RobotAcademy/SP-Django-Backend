from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel_account.controller.views import TravelAccountView

router = DefaultRouter()
router.register(r'travel_account', TravelAccountView, basename='travel_account')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check',TravelAccountView.as_view({'post': 'checkEmailDuplication'}),name='travel_account-email-duplication-check'),
    path('nickname-duplication-check',TravelAccountView.as_view({'post': 'checkNicknameDuplication'}),name='travel_account-nickname-duplication-check'),
    path('register',TravelAccountView.as_view({'post': 'registerTravelAccount'}),name='register-travel_account'),
]