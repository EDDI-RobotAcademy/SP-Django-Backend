from abc import ABC, abstractmethod

class TravelAccountService(ABC):

    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def checkNicknameDuplication(self, nickname):
        pass

    @abstractmethod
    def registerTravelAccount(self, loginType, roleType, nickname, email):
        pass