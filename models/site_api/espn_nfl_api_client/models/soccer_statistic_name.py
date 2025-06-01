from enum import Enum


class SoccerStatisticName(str, Enum):
    APPEARANCES = "appearances"
    FOULSCOMMITTED = "foulsCommitted"
    GOALASSISTS = "goalAssists"
    POSSESSIONPCT = "possessionPct"
    SHOTASSISTS = "shotAssists"
    SHOTSONTARGET = "shotsOnTarget"
    TOTALGOALS = "totalGoals"
    TOTALSHOTS = "totalShots"
    WONCORNERS = "wonCorners"

    def __str__(self) -> str:
        return str(self.value)
