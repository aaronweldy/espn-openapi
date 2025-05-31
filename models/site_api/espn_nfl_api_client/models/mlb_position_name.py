from enum import Enum


class MLBPositionName(str, Enum):
    CATCHER = "Catcher"
    CENTER_FIELD = "Center Field"
    CLOSER = "Closer"
    DESIGNATED_HITTER = "Designated Hitter"
    FIRST_BASE = "First Base"
    INFIELDER = "Infielder"
    LEFT_FIELD = "Left Field"
    OUTFIELDER = "Outfielder"
    PITCHER = "Pitcher"
    RELIEF_PITCHER = "Relief Pitcher"
    RIGHT_FIELD = "Right Field"
    SECOND_BASE = "Second Base"
    SHORTSTOP = "Shortstop"
    STARTING_PITCHER = "Starting Pitcher"
    THIRD_BASE = "Third Base"
    UTILITY = "Utility"

    def __str__(self) -> str:
        return str(self.value)
