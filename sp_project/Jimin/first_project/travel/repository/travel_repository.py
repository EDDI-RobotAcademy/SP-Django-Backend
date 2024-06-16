from abc import abstractmethod, ABC

class TravelRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, travelName, travelLocation, travelProperty, travelContent, travelPrice, travelImage):
        pass