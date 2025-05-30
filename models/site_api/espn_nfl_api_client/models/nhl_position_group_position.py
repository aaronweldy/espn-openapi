from enum import Enum


class NhlPositionGroupPosition(str, Enum):
    CENTERS = "Centers"
    DEFENSE = "Defense"
    GOALIES = "Goalies"
    LEFT_WINGS = "Left Wings"
    RIGHT_WINGS = "Right Wings"

    def __str__(self) -> str:
        return str(self.value)
