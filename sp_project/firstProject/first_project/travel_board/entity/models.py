from django.db import models

from travel_board.entity.pointchoices import PointChoices


# Create your models here.
class TravelBoard(models.Model):
    boardId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    point = models.CharField(max_length=4, choices=PointChoices.choices(), default=PointChoices.ZERO.value)
    review = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'travel_board'