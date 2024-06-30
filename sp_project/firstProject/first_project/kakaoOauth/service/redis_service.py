from abc import ABC, abstractmethod

class RedisService(ABC):
    @abstractmethod
    def storeAccessToken(self, account_id, access_token):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def deleteKey(self, key):
        pass