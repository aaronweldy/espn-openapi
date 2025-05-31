from enum import Enum


class GetRankingsSport(str, Enum):
    BASKETBALL = "basketball"
    FOOTBALL = "football"

    def __str__(self) -> str:
        return str(self.value)
