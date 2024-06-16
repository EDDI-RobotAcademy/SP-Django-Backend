from travel.repository.travel_repository_impl import TravelRepositoryImpl
from travel.service.travel_service import TravelService

class TravelServiceImpl(TravelService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__travelRepository = TravelRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return self.__travelRepository.list()

    def createTravel(self, travelName, travelPrice, travelContent,
                     travelLocation, travelProperty, travelImage):

        return self.__travelRepository.create(travelName, travelPrice, travelContent,
                     travelLocation, travelProperty, travelImage)