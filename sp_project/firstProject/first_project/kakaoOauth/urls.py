from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kakaoOauth.controller.views import KakaoOauthView

router = DefaultRouter()
router.register(r'kakaoOauth', KakaoOauthView, basename='kakaoOauth')

urlpatterns = [
    path('', include(router.urls)),

]