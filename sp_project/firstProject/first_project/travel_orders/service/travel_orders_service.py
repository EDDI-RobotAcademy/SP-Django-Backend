from abc import ABC, abstractmethod

class TravelOrderService(ABC):

    @abstractmethod
    def createOrder(self, accountId, orderItemList):
        pass