from rest_framework import viewsets, status
from rest_framework.response import Response
from travel.entity.models import Travel
from travel.serializer import TravelSerializer
from travel.service.travel_service_impl import TravelServiceImpl

class TravelView(viewsets.ViewSet):
    queryset = Travel.objects.all()

    travelService = TravelServiceImpl.getInstance()

    def list(self, request):
        travellist = self.travelService.List()
        serializer = TravelSerializer(travellist, many=True)
        return Response(serializer.data)