from abc import ABC, abstractmethod
# 240621
class TravelReviewRepository(ABC):
    @abstractmethod
    def list(self):
        pass
    @abstractmethod
    def create(self, title, point, writer, review, reviewimage):
        pass

    @abstractmethod
    def findByTravelReviewId(self, travelReviewId):
        pass

    @abstractmethod
    def deleteByTravelReviewId(self, travelReviewId):
        pass

    @abstractmethod
    def update(self, travelReviewId, travelReviewData):
        pass



