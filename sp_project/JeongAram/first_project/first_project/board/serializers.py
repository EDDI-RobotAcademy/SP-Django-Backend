from rest_framework import serializers
from board.entity.models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = []