from abc import abstractmethod, ABC

class TravelService(ABC):
    @abstractmethod
    def list(self):
        pass