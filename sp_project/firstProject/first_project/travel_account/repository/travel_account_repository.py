from abc import ABC, abstractmethod


class TravelAccountRepository(ABC):
    @abstractmethod
    def create(self, loginType, roleType):
        pass

    @abstractmethod
    def findById(self, accountId):
        pass
