from abc import ABC, abstractmethod


class TravelOrdersItemRepository(ABC):

    @abstractmethod
    def create(self, orders, travel, price):
        pass

    @abstractmethod
    def findAllByOrder(self, order):
        pass