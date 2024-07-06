from abc import ABC, abstractmethod

class TravelOrderService(ABC):

    @abstractmethod
    def createOrder(self, accountId, orderItemList):
        pass

    @abstractmethod
    def readOrderDetails(self, orderId, accountId):
        pass

    @abstractmethod
    def travelOrderList(self, accountId):
        pass