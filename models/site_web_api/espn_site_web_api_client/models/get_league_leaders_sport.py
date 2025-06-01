from enum import Enum


class GetLeagueLeadersSport(str, Enum):
    BASEBALL = "baseball"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    HOCKEY = "hockey"

    def __str__(self) -> str:
        return str(self.value)
