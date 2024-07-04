import requests

from kakaoOauth.service.kakao_oauth_service import KakaoOauthService
from first_project import settings

class KakaoOauthServiceImpl(KakaoOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            from first_project import settings
            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            cls.__instance.userinfoRequestUri = settings.KAKAO['USERINFO_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def kakaoLoginAddress(self):
        # 메서드 호출 시 메시지 출력
        print("kakaoLoginAddress()")
        # 카카오 로그인 URL을 생성하여 반환
        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")

    def requestAccessToken(self, kakaoAuthCode):
        print("requestAccessToken()") # 메서드 호출 시 메시지 출력

        # accessToken 요청을 위한 폼 데이터 작성
        accessTokenRequestForm = {
            'grant_type': 'authorization_code',  # 인증 코드 유형
            'client_id': self.clientId,          # 클라이언트 ID
            'redirect_uri': self.redirectUri,    # 인증 후 리디렉션될 URL
            'code': kakaoAuthCode,          # 클라이언트로부터 받은 인증 코드
            # 'client_secret': None
        }

        # 디버깅을 위해 요청 정보를 출력
        print(f"client_id: {self.clientId}")
        print(f"redirect_uri: {self.redirectUri}")
        print(f"code: {kakaoAuthCode}")
        print(f"tokenRequestUri: {self.tokenRequestUri}")

        # 카카오 서버에 HTTP POST 요청을 보냄
        response = requests.post(self.tokenRequestUri, data=accessTokenRequestForm)
        print(f"response: {response}")
        # 응답 데이터를 JSON 형식으로 반환
        return response.json()

    def requestUserInfo(self, accessToken):
        # HTTP 요청 시 헤더를 통해 사용자 인증
        headers = {'Authorization': f'Bearer {accessToken}'}
        response = requests.post(self.userinfoRequestUri, headers=headers)
        return response.json()


