from abc import ABC, abstractmethod
class TravelBoardRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, travelBoardData):
        pass

    @abstractmethod
    def findByTravelBoardId(self, travelBoardId):
        pass

    @abstractmethod
    def deleteByTravelBoardId(self, travelBoardId):
        pass