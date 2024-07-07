from abc import ABC, abstractmethod

class SurveyRepository(ABC):
    @abstractmethod
    def create(self, surveyData):
        pass