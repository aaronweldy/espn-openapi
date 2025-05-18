from enum import Enum


class PositionGroupPosition(str, Enum):
    CENTER = "Center"
    CORNERBACK = "Cornerback"
    DEFENSE = "defense"
    DEFENSIVE_END = "Defensive End"
    DEFENSIVE_TACKLE = "Defensive Tackle"
    FULLBACK = "Fullback"
    GUARD = "Guard"
    INJUREDRESERVEOROUT = "injuredReserveOrOut"
    INSIDE_LINEBACKER = "Inside Linebacker"
    LONG_SNAPPER = "Long Snapper"
    OFFENSE = "offense"
    OFFENSIVE_GUARD = "Offensive Guard"
    OFFENSIVE_TACKLE = "Offensive Tackle"
    OUTSIDE_LINEBACKER = "Outside Linebacker"
    PLACE_KICKER = "Place Kicker"
    PRACTICESQUAD = "practiceSquad"
    PUNTER = "Punter"
    QUARTERBACK = "Quarterback"
    RUNNING_BACK = "Running Back"
    SAFETY = "Safety"
    SPECIALTEAM = "specialTeam"
    SUSPENDED = "suspended"
    TIGHT_END = "Tight End"
    WIDE_RECEIVER = "Wide Receiver"

    def __str__(self) -> str:
        return str(self.value)
