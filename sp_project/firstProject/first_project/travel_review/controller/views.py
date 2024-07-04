from django.shortcuts import render
from rest_framework.response import Response
# 240621
# Create your views here.
from rest_framework import viewsets, status

from travel_review.entity.models import TravelReview
from travel_review.serializers import TravelReviewSerializer
from travel_review.service.travel_review_service_impl import TravelReviewServiceImpl


class TravelReviewView(viewsets.ViewSet):
    queryset = TravelReview.objects.all()

    travelReviewService = TravelReviewServiceImpl.getInstance()

    def list(self, request):
        travelReviewList = self.travelReviewService.list()
        serializer = TravelReviewSerializer(travelReviewList, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = request.data

            reviewImage = request.FILES.get('reviewImage')
            title = data.get('title')
            point = data.get('point')
            writer = data.get('writer')
            review = data.get('review')

            if not all([reviewImage, title, point, writer, review]):
                return Response({'error': '모든 내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            self.travelReviewService.createTravelReview(title, point, writer,
                                              review, reviewImage)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        travel_review = self.travelReviewService.readTravelReview(pk)
        serializer = TravelReviewSerializer(travel_review)
        return Response(serializer.data)

    def removeTravelReview(self, request, pk=None):
        self.travelReviewService.removeTravelReview(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyTravelReview(self, request, pk=None):

        try:
            # pk를 가지고 기존(old)의 객체 반환
            travel_review = self.travelReviewService.readTravelReview(pk)
            if not travel_review:
                return Response({'error': '해당 id의 리뷰를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

            # serializer에서 계속 걸려서 일단 serializer 없이 시도
            updatedTravelReview = self.travelReviewService.updateTravelReview(pk, request.data)
            return Response(TravelReviewSerializer(updatedTravelReview).data, status=status.HTTP_200_OK)

            #serializer = TravelBoardSerializer(travel_review, data=request.data, partial=True)
            # if serializer.is_valid():
            #     print('modify controller')
            #     # 시리얼라이저 거쳐 검증된 데이터로 업데이트 진행
            #     # 업데이트된 객체(updatedTravelBoard)를 Vue에 전달한다.
            #     updatedTravelBoard = self.travelBoardService.updateTravelBoard(pk, serializer.validated_data)
            #     return Response(TravelBoardSerializer(updatedTravelBoard).data, status=status.HTTP_200_OK)
            # # 만약 유효하지 않은 데이터라면 아래 반응이 나온다.
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('수정 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

