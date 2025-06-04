from enum import Enum


class GetChallengeLeaderboardView(str, Enum):
    DETAILS = "details"
    RANKS = "ranks"

    def __str__(self) -> str:
        return str(self.value)
