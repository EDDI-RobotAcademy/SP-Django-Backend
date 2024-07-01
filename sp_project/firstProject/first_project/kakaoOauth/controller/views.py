import uuid

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from kakaoOauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakaoOauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakaoOauth.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
from kakaoOauth.service.redis_service_impl import RedisServiceImpl
from travel_account.service.travel_account_service_impl import TravelAccountServiceImpl


# Create your views here.
class KakaoOauthView(viewsets.ViewSet):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()
    travelAccountService = TravelAccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    def kakaoOauthURI(self, request):
        # 카카오 로그인 주소 생성
        url = self.kakaoOauthService.kakaoLoginAddress()
        print(f"url", url)

        # 시리얼라이저를 사용해 데이터 초기화
        serializer = KakaoOauthUrlSerializer(data={ 'url': url })

        # 데이터 검증(유효하지 않으면 예외가 발생함)
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")

        # 검증된 데이터를 응답으로 반환
        return Response(serializer.validated_data)

    def kakaoAccessTokenURI(self, request):
        # 요청 데이터로 시리얼라이저 초기화
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        # 시리얼라이저를 사용하여 데이터 유효성 검사
        serializer.is_valid(raise_exception=True)
        # 유효한 데이터에서 code 값을 추출
        code = serializer.validated_data['code']
        print(f"code : {code}")
        try:
            # 인증 코드를 사용하여 accessToken 요청
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            print(f"kakaoAccessTokenURI accessToken : {accessToken}")

            # accessToken을 JSON 응답으로 반환
            return JsonResponse({'accessToken': accessToken})

        except Exception as e:
            # 예외 발생 시 에러 메시지를 JSON 응답으로 반환
            return JsonResponse({'error': str(e)}, status=500)

    def kakaoUserInfoURI(self, request):
        accessToken = request.data.get('access_token')
        print(f'kakaoUserInfoURI accessToken: {accessToken}')

        try:
            user_info = self.kakaoOauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    def redisAccessToken(self, request):
        try:
            email = request.data.get('email')
            access_token = request.data.get('accessToken')
            # 이메일 받아오는지 확인
            print(f"redisAccessToken -> email: {email}")

            # email을 받아오기 때문에 email로 account를 찾는다.
            account = self.travelAccountService.findAccountByEmail(email)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            # 랜덤한 값을 만들어 userToken으로 준다.
            # random함수를 사용하는 것 보다 중복가능성이 낮아 uuid4를 사용
            userToken = str(uuid.uuid4())
            self.redisService.storeAccessToken(account.id, userToken)

            accountId = self.redisService.getValueByKey(userToken)
            print(f"after redis' convert accountId: {accountId}")

            return Response({'userToken': userToken}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)

            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print('레디스 토큰 해제 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

