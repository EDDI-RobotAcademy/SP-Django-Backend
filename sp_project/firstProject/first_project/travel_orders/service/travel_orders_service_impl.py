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
            # print(f"registerDate: {orderItemList[-1]['registerDate']}") # 날짜 뽑기
            travel_orders = self.__travelOrdersRepository.create(accountId, TravelOrdersStatus.PENDING, orderItemList[-1]['registerDate']) # 확인이 안된 정보 Pending
            for item in orderItemList:
                print(f"order item : {item}")
                # 주문 정보가 담긴 ordersItem 객체 생성
                self.__travelOrdersItemRepository.create(
                    travel_orders, # 주문번호(ID), 계정정보 담김
                    self.__travelRepository.findByTravelId(item['travelId']), # travel 객체 정보
                    item['orderPrice'], # 상품 가격 담김
                )
            return travel_orders.id

        except Exception as e:
            print('Error Creating order:', e)
            raise e

    def readOrderDetails(self, orderId, accountId):
        try:
            order = self.__travelOrdersRepository.findById(orderId)
            print(f"travel order : {order}")
            # print(f"order.account.id: {order.account.id}, accountId: {accountId}")
            # print(f"type(order.account.id): {type(order.account.id)}, type(accountId): {type(accountId)}")
            if order.account.id != int(accountId):
                raise ValueError('Invalid accountId for this order')

            print("check order object <- readOrderDetails()")

            # OrdersItemRepositoryImpl을 통해 해당 주문의 상세 항목들을 조회합니다.
            ordersItemList = self.__travelOrdersItemRepository.findAllByOrder(order)

            # 조회된 주문 상세 내역을 필요한 형식으로 반환할 수 있도록 구성합니다.
            order_details = {
                'order': {
                    'id': order.id,
                    'status': order.status,
                    'created_date': order.created_date,

                },
                'order_items': [
                    {
                        'travel_id': item.travel_id,
                        'travel_name': self.__travelRepository.findByTravelId(item.travel_id).travelName,
                        'price': item.price,
                    }
                    for item in ordersItemList
                ]
            }

            return order_details

        except Exception as e:
            print('Error reading order details:', e)
            raise e

    def travelOrderList(self, accountId):
        ordersList = self.__travelOrdersRepository.findOrderByAccountId(accountId)
        print(f"ordersList : {ordersList}")
        return ordersList