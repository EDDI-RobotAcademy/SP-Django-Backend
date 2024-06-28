from django.db import models


class TravelAccountLoginType(models.Model):
    class LoginType(models.TextChoices):
        KAKAO = 'KAKAO', 'Kakao'

    loginType = models.CharField(max_length=10, choices=LoginType.choices)

    def __str__(self):
        return self.loginType

    class Meta:
        db_table = 'travel_account_login_type'
        app_label = 'travel_account'