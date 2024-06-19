from first_project import settings
from travel_board.entity.models import TravelBoard
from travel_board.repository.travel_board_repository import TravelBoardRepository
import os
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

    # def create(self, travelBoardData):
    #     travel_board = TravelBoard(**travelBoardData)
    #     travel_board.save()
    #     return travel_board
    def create(self, title, point, writer, review, reviewimage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            '../../../../SP-Vue-Frontend/potato/src/assets/images/uploadImages'
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, reviewimage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in reviewimage.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        travel_board = TravelBoard(
            title=title,
            review=review,
            writer=writer,
            point=point,
            reviewImage=reviewimage.name
        )
        travel_board.save()
        return travel_board

    def findByTravelBoardId(self, travelBoardId):
        return TravelBoard.objects.get(boardId=travelBoardId)

    def update(self, travel_board, travelBoardData):
        for key, value in travelBoardData.items():
            print(f"key: {key}, value: {value}")

            setattr(travel_board, key, value)

        travel_board.save()
        return travel_board



