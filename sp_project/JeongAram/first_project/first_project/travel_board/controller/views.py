from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from travel_board.entity.models import TravelBoard
from travel_board.serializers import TravelBoardSerializer

class TravelBoardView(viewsets.ViewSet):
    queryset = TravelBoard.objects.all()