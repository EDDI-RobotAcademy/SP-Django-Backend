from abc import ABC, abstractmethod


class TravelService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def checkNicknameDuplication(self, nickname):
        pass

    @abstractmethod
    def registerAccount(self, loginType, roleType, nickname, email):
        pass
