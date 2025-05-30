from enum import Enum


class GetScoreboardSport(str, Enum):
    BASEBALL = "baseball"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    HOCKEY = "hockey"

    def __str__(self) -> str:
        return str(self.value)
