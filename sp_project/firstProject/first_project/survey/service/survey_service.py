from abc import ABC, abstractmethod

class SurveyService(ABC):
    @abstractmethod
    def createSurvey(self, surveyData):
        pass

