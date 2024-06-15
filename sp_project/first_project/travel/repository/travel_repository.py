from abc import ABC, abstractmethod


class TravelRepository(ABC):
    @abstractmethod
    def list(self):
        pass

