from rest_framework import viewsets, status
from rest_framework.response import Response
from kakaoOauth.service.redis_service_impl import RedisServiceImpl
from travel_orders.service.travel_orders_service_impl import TravelOrderServiceImpl
class TravelOrdersView(viewsets.ViewSet):
    travelOrderService = TravelOrderServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()