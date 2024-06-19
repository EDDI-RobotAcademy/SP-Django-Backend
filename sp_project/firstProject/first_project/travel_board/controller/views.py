from django.shortcuts import render
from rest_framework.response import Response

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
        # print(request.data)
        # serializer = TravelBoardSerializer(data=request.data)
        # if serializer.is_valid():
        #     travel_board = self.travelBoardService.createTravelBoard(serializer.validated_data)
        #     return Response(TravelBoardSerializer(travel_board).data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        travel_board = self.travelBoardService.readBoard(pk)
        serializer = TravelBoardSerializer(travel_board)
        return Response(serializer.data)


    def read(self, request, pk=None):
        travel_board = self.travelBoardService.readTravelBoard(pk)
        serializer = TravelBoardSerializer(travel_board)
        return Response(serializer.data)


    def modifyTravelBoard(self, request, pk=None):
        travel_board = self.travelBoardService.readTravelBoard(pk)
        serializer = TravelBoardSerializer(travel_board, data=request.data, partial=True)

        if serializer.is_valid():
            updatedTravelBoard = self.travelBoardService.updateTravelBoard(pk, serializer.validated_data)
            return Response(TravelBoardSerializer(updatedTravelBoard).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

