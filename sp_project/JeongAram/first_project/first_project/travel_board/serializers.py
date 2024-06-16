from rest_framework import serializers

from travel_board.entity.models import TravelBoard


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class TravelBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelBoard
        fields = ['travelId', 'travelName', 'travelPrice',
                  'travelLocation', 'travelProperty', 'travelContent', 'travelImage']

