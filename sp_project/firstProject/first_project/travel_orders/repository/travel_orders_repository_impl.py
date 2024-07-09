from travel_orders.entity.travel_orders import TravelOrders
from travel_orders.repository.travel_orders_repository import TravelOrdersRepository

class TravelOrdersRepositoryImpl(TravelOrdersRepository):
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

    def create(self, accountId, status, date):
        orders = TravelOrders(account_id=accountId, status=status, created_date=date)
        orders.save()

        return orders

    def findById(self, orderId):
        return TravelOrders.objects.get(id=orderId)

    def findOrderByAccountId(self, accountId):
        return TravelOrders.objects.filter(account_id=accountId)
        #get(account_id=accountId) # __str__에 선언 된게 반환 됨
        # [<TravelOrders: TravelOrders 1 by TravelAccount -> id: 1, loginType: KAKAO, roleType: NORMAL>