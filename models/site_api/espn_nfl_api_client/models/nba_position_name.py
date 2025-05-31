from enum import Enum


class NBAPositionName(str, Enum):
    CENTER = "Center"
    FORWARD = "Forward"
    FORWARD_CENTER = "Forward-Center"
    GUARD = "Guard"
    GUARD_FORWARD = "Guard-Forward"
    POINT_GUARD = "Point Guard"
    POWER_FORWARD = "Power Forward"
    SHOOTING_GUARD = "Shooting Guard"
    SMALL_FORWARD = "Small Forward"

    def __str__(self) -> str:
        return str(self.value)
