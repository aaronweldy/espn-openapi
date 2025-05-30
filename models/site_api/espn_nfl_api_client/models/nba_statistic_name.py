from enum import Enum


class NbaStatisticName(str, Enum):
    ASSISTS = "assists"
    AVGASSISTS = "avgAssists"
    AVGPOINTS = "avgPoints"
    AVGREBOUNDS = "avgRebounds"
    FIELDGOALPCT = "fieldGoalPct"
    FIELDGOALSATTEMPTED = "fieldGoalsAttempted"
    FIELDGOALSMADE = "fieldGoalsMade"
    FREETHROWPCT = "freeThrowPct"
    FREETHROWSATTEMPTED = "freeThrowsAttempted"
    FREETHROWSMADE = "freeThrowsMade"
    POINTS = "points"
    REBOUNDS = "rebounds"
    THREEPOINTFIELDGOALPCT = "threePointFieldGoalPct"
    THREEPOINTFIELDGOALSATTEMPTED = "threePointFieldGoalsAttempted"
    THREEPOINTFIELDGOALSMADE = "threePointFieldGoalsMade"
    THREEPOINTPCT = "threePointPct"
    THREESMADE = "threesMade"

    def __str__(self) -> str:
        return str(self.value)
