from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.entity.models import Survey
from survey.serializers import SurveySerializer
from survey.service.survey_service_impl import SurveyServiceImpl


class SurveyView(viewsets.ViewSet):
    # queryset = Survey.objects.all()
    surveyService = SurveyServiceImpl.getInstance()

    def register(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            survey = self.surveyService.createSurvey(serializer.validated_data)
            return Response(SurveySerializer(survey).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




