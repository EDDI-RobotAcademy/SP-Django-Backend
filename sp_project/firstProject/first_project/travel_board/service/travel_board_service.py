from abc import ABC, abstractmethod
# 240621
class TravelBoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravelBoard(self, title, point, writer, review, reviewimage):
        pass
    @abstractmethod
    def readTravelBoard(self, travelBoardId):
        pass
    @abstractmethod
    def removeTravelBoard(self, travelBoardId):
        pass
    @abstractmethod
    def updateTravelBoard(self, travelBoardId, travelBoardData):
        pass


