from abc import ABC,abstractmethod

class TravelService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravel(self, travelName, travelPrice, travelProperty,
                     travelContent, travelImage):
        pass

    @abstractmethod
    def readTravel(self, travelId):
        pass