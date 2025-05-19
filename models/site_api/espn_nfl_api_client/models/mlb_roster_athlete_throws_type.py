from enum import Enum


class MlbRosterAthleteThrowsType(str, Enum):
    BOTH = "BOTH"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
