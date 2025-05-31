from enum import Enum


class NFLPositionName(str, Enum):
    CENTER = "Center"
    CORNERBACK = "Cornerback"
    DEFENSIVE_BACK = "Defensive Back"
    DEFENSIVE_END = "Defensive End"
    DEFENSIVE_TACKLE = "Defensive Tackle"
    FULLBACK = "Fullback"
    GUARD = "Guard"
    INSIDE_LINEBACKER = "Inside Linebacker"
    LINEBACKER = "Linebacker"
    LONG_SNAPPER = "Long Snapper"
    OFFENSIVE_GUARD = "Offensive Guard"
    OFFENSIVE_TACKLE = "Offensive Tackle"
    OUTSIDE_LINEBACKER = "Outside Linebacker"
    PLACE_KICKER = "Place kicker"
    PUNTER = "Punter"
    QUARTERBACK = "Quarterback"
    RUNNING_BACK = "Running Back"
    SAFETY = "Safety"
    TIGHT_END = "Tight End"
    WIDE_RECEIVER = "Wide Receiver"

    def __str__(self) -> str:
        return str(self.value)
