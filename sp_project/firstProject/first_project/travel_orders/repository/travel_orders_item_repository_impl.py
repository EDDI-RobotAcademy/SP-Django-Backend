from travel_orders.entity.travel_orders_item import TravelOrdersItem
from travel_orders.repository.travel_orders_item_repository import TravelOrdersItemRepository

class TravelOrdersItemRepositoryImpl(TravelOrdersItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, orders, travel, price):
        # 입력 데이터에 맞게 OrdersItem field 내용 저장
        order_item = TravelOrdersItem(orders=orders, travel=travel, price=price)
        order_item.save()

    def findAllByOrder(self, order):
        return TravelOrdersItem.objects.filter(orders=order)