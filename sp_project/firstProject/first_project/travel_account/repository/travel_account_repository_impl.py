

from travel_account.entity.travel_account import TravelAccount
from travel_account.entity.travel_account_login_type import TravelAccountLoginType
from travel_account.entity.travel_account_role_type import TravelAccountRoleType
from travel_account.repository.travel_account_repository import TravelAccountRepository

class TravelAccountRepositoryImpl(TravelAccountRepository):
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


    def create(self, loginType, roleType):
        # '_' 보편적으로 언더바는 별 의미가 없는 데이터를 받는 경우 사용하지 않는다의 관습적 표현
        loginTypeEntity, _ = TravelAccountLoginType.objects.get_or_create(loginType=loginType)
        roleTypeEntity, _ = TravelAccountRoleType.objects.get_or_create(roleType=roleType)

        travel_account = TravelAccount.objects.create(loginType=loginTypeEntity, roleType=roleTypeEntity)
        return travel_account


    def findById(self, accountId):
        travel_account = TravelAccount.objects.get(id=accountId)
        return travel_account

