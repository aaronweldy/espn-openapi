from enum import Enum


class NHLPositionName(str, Enum):
    CENTER = "Center"
    DEFENSE = "Defense"
    DEFENSEMAN = "Defenseman"
    FORWARD = "Forward"
    GOALIE = "Goalie"
    GOALTENDER = "Goaltender"
    LEFT_WING = "Left Wing"
    RIGHT_WING = "Right Wing"

    def __str__(self) -> str:
        return str(self.value)
