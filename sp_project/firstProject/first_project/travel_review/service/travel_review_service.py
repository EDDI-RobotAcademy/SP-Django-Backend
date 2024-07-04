from abc import ABC, abstractmethod
# 240621
class TravelReviewService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createTravelReview(self, title, point, writer, review, reviewimage):
        pass
    @abstractmethod
    def readTravelReview(self, travelReviewId):
        pass
    @abstractmethod
    def removeTravelReview(self, travelReviewId):
        pass

    @abstractmethod
    def updateTravelReview(self, travelReviewId, travelReviewData):
        pass


