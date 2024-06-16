from abc import abstractmethod, ABC

class TravelService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravel(self, travelName, travelLocation, travelProperty, travelContent, travelPrice, travelImage):
        pass