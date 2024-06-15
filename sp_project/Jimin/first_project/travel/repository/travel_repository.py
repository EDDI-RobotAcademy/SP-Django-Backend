from abc import abstractmethod, ABC

class TravelRepository(ABC):
    @abstractmethod
    def list(self):
        pass