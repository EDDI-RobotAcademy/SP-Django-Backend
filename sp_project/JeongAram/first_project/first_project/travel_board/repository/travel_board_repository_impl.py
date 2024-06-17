from travel_board.entity.models import TravelBoard
from travel_board.repository.travel_board_repository import TravelBoardRepository
class TravelBoardRepositoryImpl(TravelBoardRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return TravelBoard.objects.all().order_by('-regDate')

    def create(self, travelBoardData):
        travel_board = TravelBoard(**travelBoardData)
        travel_board.save()
        return travel_board