from abc import ABC,abstractmethod

class TravelService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravel(self, travelName, travelLocation, travelPrice,
                     travelProperty, travelContent, travelImage):
        pass