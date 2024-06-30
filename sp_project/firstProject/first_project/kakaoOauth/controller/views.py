from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from kakaoOauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakaoOauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakaoOauth.service.kakao_oauth_service_impl import KakaoOauthServiceImpl


# Create your views here.
class KakaoOauthView(viewsets.Viewset):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()


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

        try:
            # 인증 코드를 사용하여 accessToken 요청
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            # accessToken을 JSON 응답으로 반환
            return JsonResponse({'accessToken': accessToken})
        except Exception as e:
            # 예외 발생 시 에러 메시지를 JSON 응답으로 반환
            return JsonResponse({'error': str(e)}, status=500)

    def kakaoUserInfoURI(self, request):
        accessToken = self.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            user_info = self.kakaoOauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)




