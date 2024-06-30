from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from travel_account.serilaizers import TravelAccountSerializer
from travel_account.service.travel_account_service_impl import TravelAccountServiceImpl


class TravelAccountView(viewsets.ViewSet):
    travelAccountService = TravelAccountServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.travelAccountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'massage': ' 이미 가입된 Email입니다.'\
                             if isDuplicate else '사용 가능한 Email입니다.'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def checkNicknameDuplication(self, request):
        print("checkNicknameDuplication()")

        try:
            nickname = request.data.get('newNickname')
            print(f"nickname: {nickname}")
            isDuplicate = self.travelAccountService.checkNicknameDuplication(nickname)

            return Response({'isDuplicate': isDuplicate, 'message': '이미 사용 중인 Nickname 입니다.' \
                             if isDuplicate else '사용 가능한 Nickname 입니다.'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def registerTravelAccount(self, request):
        try:
            nickname = request.data.get('nickname')
            email = request.data.get('email')

            travel_account = self.travelAccountService.registerTravelAccount(
                loginType='KAKAO',
                roleType='NORMAL',
                nickname=nickname,
                email=email,
            )

            serializer = TravelAccountSerializer(travel_account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)