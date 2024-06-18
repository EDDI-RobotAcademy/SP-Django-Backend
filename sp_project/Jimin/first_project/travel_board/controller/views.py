from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl


# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class TravelBoardView(viewsets.ViewSet):
    queryset = TravelBoard.objects.all()
    travelBoardService = TravelBoardServiceImpl.getInstance()

    def list(self, request):
        travelBoardList = self.travelBoardService.list()
        serializer = BoardSerializer(travelBoardList, many=True)
        return Response(serializer.data)