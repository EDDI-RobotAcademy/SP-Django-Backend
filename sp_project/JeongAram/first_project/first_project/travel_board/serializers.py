from rest_framework import serializers

from travel_board.entity.models import TravelBoard


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class TravelBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelBoard
        fields = ['boardId', 'title', 'writer', 'point', 'review']
        read_only_fields = ['regDate', 'updDate']

