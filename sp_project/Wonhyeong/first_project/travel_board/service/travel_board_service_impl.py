from travel_board.repository.travel_board_repository_impl import TravelBoardRepositoryImpl
from travel_board.service.travel_board_service import TravelBoardService

class TravelBoardServiceImpl(TravelBoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__travelBoardRepository = TravelBoardRepositoryImpl.getInstance()
            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__travelBoardRepository.list()

    def createTravelBoard(self, travelBoardData):
        return self.__travelBoardRepository.create(travelBoardData)

    def readTravelBoard(self, boardId):
        return self.__travelBoardRepository.findByBoardId(boardId)