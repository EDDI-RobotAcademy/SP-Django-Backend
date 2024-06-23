from first_project import settings
from travel_board.entity.models import TravelBoard
from travel_board.repository.travel_board_repository import TravelBoardRepository
import os
# 240621
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

    def deleteByTravelBoardId(self, travelBoardId):
        travel_board = TravelBoard.objects.get(boardId=travelBoardId)
        travel_board.delete()

    def update(self, travel_board, travelBoardData):
        print(f"travel_board repository update()")
        # 이미지만 수정
        # 요청에 이미지가 진짜 있다면, 새 이미지로 교체
        if 'reviewImage' in travelBoardData:  # if travelBoardData['reviewImage'] != null
            new_image = travelBoardData['reviewImage']
            if new_image:
                # 필요한 경우 기존 이미지 삭제
                if travel_board.reviewImage:
                    # 현석이가 짠 delete함수 출력하면 됨 (repository의 delete 함수에 삭제요청 보내기)
                    #self.delete(travel_board.reviewImage.path)
                    #travel_board.delete()
                    # db field인 reviewImage 이름이 new_image의 이름으로 바뀜
                    travel_board.reviewImage = new_image

        # 나머지 필드 업데이트
        for key, value in travelBoardData.items():
            # reviewImage field 빼고 다 업데이트
            if key != 'reviewImage':
                setattr(travel_board, key, value)

        travel_board.save()
        return travel_board


    # 파일 이름 삭제하고 새로 업





