from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from board.entity.models import Board
from board.serializers import BoardSerializer

class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()