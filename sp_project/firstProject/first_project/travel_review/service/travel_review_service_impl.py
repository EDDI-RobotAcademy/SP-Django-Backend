from travel_review.repository.travel_review_repository_impl import TravelReviewRepositoryImpl
from travel_review.service.travel_review_service import TravelReviewService
# 240621
class TravelReviewServiceImpl(TravelReviewService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__travelReviewRepository = TravelReviewRepositoryImpl.getInstance()
            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__travelReviewRepository.list()

    def createTravelReview(self, title, point, writer, review, reviewimage):
        return self.__travelReviewRepository.create(
            title, point, writer, review, reviewimage)

    def readTravelReview(self, travelReviewId):
        return self.__travelReviewRepository.findByTravelReviewId(travelReviewId)

    def removeTravelReview(self, travelReviewId):
        return self.__travelReviewRepository.deleteByTravelReviewId(travelReviewId)

    def updateTravelReview(self, travelReviewId, travelReviewData):
        travel_review = self.__travelReviewRepository.findByTravelReviewId(travelReviewId)
        updatedTravelReview = self.__travelReviewRepository.update(travel_review, travelReviewData)
        return updatedTravelReview
