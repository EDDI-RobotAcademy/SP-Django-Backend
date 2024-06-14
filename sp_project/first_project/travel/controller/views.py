from rest_framework import viewsets, status

from travel.entity.models import Travel


class TravelView(viewsets.ViewSet):
    queryset = Travel.objects.all()