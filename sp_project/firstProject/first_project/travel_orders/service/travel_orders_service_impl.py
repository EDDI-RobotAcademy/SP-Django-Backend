from travel.repository.travel_repository_impl import TravelRepositoryImpl
from travel_orders.service.travel_orders_service import TravelOrderService
from travel_orders.entity.travel_orders_status import TravelOrdersStatus
from travel_orders.repository.travel_orders_repository_impl import TravelOrdersRepositoryImpl
from travel_orders.repository.travel_orders_item_repository_impl import TravelOrdersItemRepositoryImpl
class TravelOrderServiceImpl(TravelOrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__travelOrdersRepository = TravelOrdersRepositoryImpl.getInstance()
            cls.__instance.__travelRepository = TravelRepositoryImpl.getInstance()
            cls.__instance.__travelOrdersItemRepository = TravelOrdersItemRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createOrder(self, accountId, orderItemList):
        try:
            # travel_orders객체 생성
            travel_orders = self.__travelOrdersRepository.create(accountId, TravelOrdersStatus.PENDING) # 확인이 안된 정보 Pending
            for item in orderItemList:
                # 주문 정보가 담긴 ordersItem 객체 생성
                self.__travelOrdersItemRepository.create(
                    travel_orders, # 주문번호(ID), 계정정보 담김
                    item['travelName'], # 상품 정보 담김
                    item['orderPrice'], # 상품 가격 담김
                )
            return travel_orders.id

        except Exception as e:
            print('Error Creating order:', e)
            raise e