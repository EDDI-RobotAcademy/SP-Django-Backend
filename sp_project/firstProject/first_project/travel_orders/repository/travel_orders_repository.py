from abc import ABC, abstractmethod


class TravelOrdersRepository(ABC):

    @abstractmethod
    def create(self, accountId, status, date):
        pass

    @abstractmethod
    def findById(self, orderId):
        pass

    @abstractmethod
    def findOrderByAccountId(self, accountId):
        pass