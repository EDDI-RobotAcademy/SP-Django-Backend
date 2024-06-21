from abc import ABC, abstractmethod
class TravelBoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravelBoard(self, travelBoardData):
        pass

    @abstractmethod
    def readTravelBoard(self, travelBoardId):
        pass


    @abstractmethod
    def removeTravelBoard(self, travelBoardId):
        pass