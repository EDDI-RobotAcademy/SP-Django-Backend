from travel_orders.service.travel_orders_service import TravelOrderService
from travel_orders.entity.travel_orders_status import TravelOrdersStatus
from travel_orders.repository.travel_orders_repository_impl import TravelOrdersRepositoryImpl
from travel_orders.repository.travel_orders_item_repository_impl import TravelOrdersItemRepositoryImpl
class TravelOrderServiceImpl(TravelOrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__ordersRepository = TravelOrdersRepositoryImpl.getInstance()
            cls.__instance.__ordersItemRepository = TravelOrdersItemRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance