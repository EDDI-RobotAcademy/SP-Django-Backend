from django.db import models

from travel_account.entity.travel_account_login_type import TravelAccountLoginType
from travel_account.entity.travel_account_role_type import TravelAccountRoleType


class TravelAccount(models.Model):
    id = models.AutoField(primary_key=True)
    loginType = models.ForeignKey(TravelAccountLoginType, on_delete=models.CASCADE)
    roleType = models.ForeignKey(TravelAccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"TravelAccount -> id: {self.id}, loginType: {self.loginType}, roleType: {self.roleType}"

    class Meta:
        db_table = 'travel_account'
        app_label = 'travel_account'

    def getId(self):
        return self.id