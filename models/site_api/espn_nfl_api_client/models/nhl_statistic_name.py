from enum import Enum


class NhlStatisticName(str, Enum):
    ASSISTS = "assists"
    GOALS = "goals"
    PLUSMINUS = "plusMinus"
    POINTS = "points"
    SAVEPCT = "savePct"
    SAVES = "saves"
    YTDGOALS = "ytdGoals"

    def __str__(self) -> str:
        return str(self.value)
