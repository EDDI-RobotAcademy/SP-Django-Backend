from travel_account.entity import travel_account
from travel_account.repository.profile_repository_impl import ProfileRepositoryImpl
from travel_account.repository.travel_account_repository_impl import TravelAccountRepositoryImpl
from travel_account.service.travel_account_service import TravelAccountService


class TravelAccountServiceImpl(TravelAccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()
            cls.__instance.__travelAccountRepository = TravelAccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def checkEmailDuplication(self, email):
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None


    def checkNicknameDuplication(self, nickname):
        profile = self.__profileRepository.findByNickname(nickname)
        return profile is not None


    def registerTravelAccount(self, loginType, roleType, nickname, email):
        travel_account = self.__travelAccountRepository.create(loginType, roleType)
        return self.__profileRepository.create(nickname, email, travel_account)

    def findAccountByEmail(self, email):
        return self.__profileRepository.findByEmail(email)
