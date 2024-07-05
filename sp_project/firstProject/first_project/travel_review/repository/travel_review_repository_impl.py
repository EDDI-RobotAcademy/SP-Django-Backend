from first_project import settings
from travel_review.entity.models import TravelReview
from travel_review.repository.travel_review_repository import TravelReviewRepository
import os
# 240621
class TravelReviewRepositoryImpl(TravelReviewRepository):
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
        return TravelReview.objects.all().order_by('-regDate')

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

        travel_review = TravelReview(
            title=title,
            review=review,
            writer=writer,
            point=point,
            reviewImage=reviewimage.name
        )
        travel_review.save()
        return travel_review

    def findByTravelReviewId(self, travelReviewId):
        return TravelReview.objects.get(reviewId=travelReviewId)

    def deleteByTravelReviewId(self, travelReviewId):
        travel_review = TravelReview.objects.get(reviewId=travelReviewId)
        travel_review.delete()

    def update(self, travel_review, travelReviewData):
        print(f"travel_review repository update()")
        # 이미지만 수정
        # 요청에 이미지가 진짜 있다면, 새 이미지로 교체
        if 'reviewImage' in travelReviewData:  # if travelBoardData['reviewImage'] != null
            new_image = travelReviewData['reviewImage']
            print(new_image)
            if new_image != 'null':
                # 필요한 경우 기존 이미지 삭제
                if travel_review.reviewImage:
                    print("바꾼 이미지 등록")
                    uploadDirectory = os.path.join(
                        settings.BASE_DIR,
                        '../../../../SP-Vue-Frontend/potato/src/assets/images/uploadImages'
                    )
                    if not os.path.exists(uploadDirectory):
                        os.makedirs(uploadDirectory)

                    imagePath = os.path.join(uploadDirectory, new_image.name)
                    with open(imagePath, 'wb+') as destination:
                        for chunk in new_image.chunks():
                            destination.write(chunk)

                        destination.flush()
                        os.fsync(destination.fileno())
                    # db field인 reviewImage 이름이 new_image의 이름으로 바뀜
                    travel_review.reviewImage = new_image
            else:
                pass

        # 나머지 필드 업데이트
        for key, value in travelReviewData.items():
            # reviewImage field 빼고 다 업데이트
            if key != 'reviewImage':
                setattr(travel_review, key, value)

        travel_review.save()
        return travel_review





