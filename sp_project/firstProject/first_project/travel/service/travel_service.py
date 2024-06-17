from abc import ABC,abstractmethod

class TravelService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravel(self, travelName, travelPrice, travelContent,
                     travelLocation, travelProperty, travelImage):
        pass