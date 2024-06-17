from enum import Enum

class PointChoices(Enum):
    ZERO = '0.00'
    ONE = '1.00'
    TWO = '2.00'
    THREE = '3.00'
    FOUR = '4.00'
    FIVE = '5.00'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]