from rest_framework import serializers

from travel_review.entity.models import TravelReview


class TravelReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelReview
        fields = ['reviewId', 'title', 'writer', 'point', 'review', 'reviewImage']
        read_only_fields = ['regDate', 'updDate']


