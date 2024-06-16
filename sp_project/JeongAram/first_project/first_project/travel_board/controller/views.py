from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets, status
from travel_board.entity.models import TravelBoard
from travel_board.serializers import TravelBoardSerializer
from travel_board.service.travel_board_service_impl import TravelBoardServiceImpl


class TravelBoardView(viewsets.ViewSet):
    queryset = TravelBoard.objects.all()

    travelBoardService = TravelBoardServiceImpl.getInstance()

    def list(self, request):
        travelBoardList = self.travelBoardService.list()
        serializer = TravelBoardSerializer(travelBoardList, many=True)
        return Response(serializer.data)


