from enum import Enum


class NhlStatisticName(str, Enum):
    ASSISTS = "assists"
    FIRSTSTAR = "firstStar"
    GOALS = "goals"
    LOSINGGOALIE = "losingGoalie"
    PLUSMINUS = "plusMinus"
    POINTS = "points"
    PROBABLESTARTINGGOALIE = "probableStartingGoalie"
    SAVEPCT = "savePct"
    SAVES = "saves"
    SECONDSTAR = "secondStar"
    THIRDSTAR = "thirdStar"
    WINNINGGOALIE = "winningGoalie"
    YTDGOALS = "ytdGoals"

    def __str__(self) -> str:
        return str(self.value)
