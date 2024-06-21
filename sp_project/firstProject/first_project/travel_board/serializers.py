from rest_framework import serializers

from travel_board.entity.models import TravelBoard

class TravelBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelBoard
        fields = ['boardId', 'title', 'writer', 'point', 'review', 'reviewImage']
        read_only_fields = ['regDate', 'updDate']


