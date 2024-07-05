from rest_framework import serializers

from travel.entity.models import Travel


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ['travelId', 'travelName', 'travelPrice',
                 'travelProperty', 'travelContent', 'travelImage']

