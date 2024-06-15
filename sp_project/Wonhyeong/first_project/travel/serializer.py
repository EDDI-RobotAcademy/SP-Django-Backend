from rest_framework import serializers

from travel.entity.models import Travel



class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ['travelId', 'travelName', 'travelLocation', 'travelProperty', 'travelContent', 'travelImage', 'registeredDate', 'updatedDate']
