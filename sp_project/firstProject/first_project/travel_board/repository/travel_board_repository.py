from abc import ABC, abstractmethod
# 240621
class TravelBoardRepository(ABC):
    @abstractmethod
    def list(self):
        pass
    @abstractmethod
    def create(self, title, point, writer, review, reviewimage):
        pass

    @abstractmethod
    def findByTravelBoardId(self, travelBoardId):
        pass

    @abstractmethod
    def deleteByTravelBoardId(self, travelBoardId):
        pass

    @abstractmethod
    def update(self, travelBoardId, travelBoardData):
        pass



