from enum import Enum

class PointChoices(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]