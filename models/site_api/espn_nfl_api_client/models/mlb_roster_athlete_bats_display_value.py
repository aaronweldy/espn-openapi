from enum import Enum


class MlbRosterAthleteBatsDisplayValue(str, Enum):
    BOTH = "Both"
    LEFT = "Left"
    RIGHT = "Right"

    def __str__(self) -> str:
        return str(self.value)
