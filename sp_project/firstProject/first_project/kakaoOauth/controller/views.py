from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class KakaoOauthView(viewsets.Viewset):
    oauthService = KakaoOauthServiceImpl.getInstance()


    def kakaoOauthURI(self, request):
        # 카카오 로그인 주소 생성
        url = self.oauthService.kakaoLoginAddress()
        print(f"url", url)

        # 시리얼라이저를 사용해 데이터 초기화
        serializer = KakaoOauthUrlSerializer(data={ 'url': url })

        # 데이터 검증(유효하지 않으면 예외가 발생함)
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")

        # 검증된 데이터를 응답으로 반환
        return Response(serializer.validated_data)




