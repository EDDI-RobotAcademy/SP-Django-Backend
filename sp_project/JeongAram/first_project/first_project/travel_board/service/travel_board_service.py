from abc import ABC, abstractmethod
class TravelBoardService(ABC):
    @abstractmethod
    def list(self):
        pass