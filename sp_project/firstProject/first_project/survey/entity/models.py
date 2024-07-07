from django.db import models

from travel_account.entity.travel_account import TravelAccount


# Create your models here.

class Survey(models.Model):
    user = models.ForeignKey(TravelAccount, on_delete=models.CASCADE, related_name='survey')
    age = models.IntegerField()
    travelConcept = models.IntegerField()
    travelCompanion = models.IntegerField()
    snsFrequency = models.IntegerField()
    photoFrequency = models.IntegerField()
    travelBudget = models.IntegerField()



    def __str__(self):
        # f"{self.user.username} - Survey {self.id}
        return

    class Meta:
        db_table = 'survey'