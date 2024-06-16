from abc import ABC,abstractmethod

class TravelRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, travelName, travelLocation, travelPrice,
                     travelProperty, travelContent, travelImage):
        pass