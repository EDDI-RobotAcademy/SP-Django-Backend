from django.utils import timezone
from travel_orders.entity.travel_orders_status import TravelOrdersStatus
from django.db import models

from travel_account.entity.travel_account import TravelAccount


class TravelOrders(models.Model):
    # 주문 일자, 마감 기한까지 등록하기 >> 근데 orders에 할지, account 정보에 할지
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(TravelAccount, on_delete=models.CASCADE, related_name='travel_orders')
    status = models.CharField(max_length=10, choices=TravelOrdersStatus.choices, default=TravelOrdersStatus.PENDING)
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}" # TravelOrders : {self.id} by {self.account}"

    class Meta:
        db_table = 'travel_orders'
        app_label = 'travel_orders'