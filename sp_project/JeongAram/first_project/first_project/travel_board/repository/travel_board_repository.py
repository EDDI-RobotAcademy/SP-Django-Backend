from abc import ABC, abstractmethod
class TravelBoardRepository(ABC):
    @abstractmethod
    def list(self):
        pass