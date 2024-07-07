from rest_framework import serializers

from survey.entity.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [ 'age', 'gender', 'travelConcept', 'travelCompanion', 'snsFrequency',
                  'photoFrequency', 'travelBudget']
