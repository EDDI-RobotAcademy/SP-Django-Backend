from abc import ABC,abstractmethod

class TravelRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, travelName, travelPrice,
                     travelProperty, travelContent, travelImage):
        pass

    @abstractmethod
    def findByTravelId(self, travelId):
        pass