from abc import ABC, abstractmethod


class TravelOrdersRepository(ABC):

    def create(self, accountId, status):
        pass