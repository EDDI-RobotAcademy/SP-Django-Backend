from django.shortcuts import render
from rest_framework.response import Response
# 240621
# Create your views here.
from rest_framework import viewsets, status
from travel_board.entity.models import TravelBoard
from travel_board.serializers import TravelBoardSerializer
from travel_board.service.travel_board_service_impl import TravelBoardServiceImpl


class TravelBoardView(viewsets.ViewSet):
    queryset = TravelBoard.objects.all()

    travelBoardService = TravelBoardServiceImpl.getInstance()

    def list(self, request):
        travelBoardList = self.travelBoardService.list()
        serializer = TravelBoardSerializer(travelBoardList, many=True)
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

            self.travelBoardService.createTravelBoard(title, point, writer,
                                              review, reviewImage)

            serializer = TravelBoardSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        travel_board = self.travelBoardService.readTravelBoard(pk)
        serializer = TravelBoardSerializer(travel_board)
        return Response(serializer.data)

    def removeTravelBoard(self, request, pk=None):
        self.travelBoardService.removeTravelBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyTravelBoard(self, request, pk=None):
        try:
            # pk를 가지고 기존(old)의 객체 반환
            travel_board = self.travelBoardService.readTravelBoard(pk)
            if not travel_board:
                return Response({'error': '해당 id의 리뷰를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

            serializer = TravelBoardSerializer(travel_board, data=request.data, partial=True)

            if serializer.is_valid():
                # 시리얼라이저 거쳐 검증된 데이터로 업데이트 진행
                # 업데이트된 객체(updatedTravelBoard)를 Vue에 전달한다.
                updatedTravelBoard = self.travelBoardService.updateTravelBoard(pk, serializer.validated_data)
                print(f"반환 성공!")
                return Response(TravelBoardSerializer(updatedTravelBoard).data, status=status.HTTP_200_OK)
            # 만약 유효하지 않은 데이터라면 아래 반응이 나온다.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('수정 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

