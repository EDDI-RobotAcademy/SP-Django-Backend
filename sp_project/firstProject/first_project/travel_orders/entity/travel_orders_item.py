from django.db import models

from travel_orders.entity.travel_orders import TravelOrders
from travel.entity.models import Travel


class TravelOrdersItem(models.Model):
    # 기간을 넣어주면 될 듯?
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(TravelOrders, related_name='travel_order_items', on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"TravelOrderItem {self.id} for TravelOrder {self.orders.id}"

    def total_price(self):
        return self.price

    class Meta:
        db_table = 'travel_orders_item'
        app_label = 'travel_orders'
