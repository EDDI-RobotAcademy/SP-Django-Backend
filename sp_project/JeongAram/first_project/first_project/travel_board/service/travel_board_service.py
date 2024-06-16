from abc import ABC, abstractmethod
class TravelBoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravelBoard(self, travelBoardData):
        pass