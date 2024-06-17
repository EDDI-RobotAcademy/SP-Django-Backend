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

    def create(self, request):
        serializer = TravelBoardSerializer(data=request.data)
        if serializer.is_valid():
            travel_board = self.travelBoardService.createTravelBoard(serializer.validated_data)
            return Response(TravelBoardSerializer(travel_board).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        travelBoard = self.travelBoardService.read(pk)
        serializer = TravelBoardSerializer(travelBoard)
        return Response(serializer.data)