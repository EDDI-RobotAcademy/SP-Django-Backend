from abc import ABC,abstractmethod


class TravelService(ABC):

    @abstractmethod
    def list(self):
        pass
