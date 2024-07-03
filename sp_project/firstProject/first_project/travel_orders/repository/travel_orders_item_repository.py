from abc import ABC, abstractmethod


class TravelOrdersItemRepository(ABC):

    def create(self, orders, travel, price):
        pass