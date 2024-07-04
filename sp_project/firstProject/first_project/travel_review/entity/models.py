from django.db import models

from travel_review.entity.pointchoices import PointChoices

# 240621
# Create your models here.
class TravelReview(models.Model):
    reviewId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    point = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()],
        default=int(PointChoices.ZERO.value))
    review = models.TextField()
    reviewImage = models.CharField(max_length=100, null=True)



    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'travel_review'