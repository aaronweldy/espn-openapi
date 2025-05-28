from enum import Enum


class NhlAthleteCatchesDisplayValue(str, Enum):
    LEFT = "Left"
    RIGHT = "Right"

    def __str__(self) -> str:
        return str(self.value)
