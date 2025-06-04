from enum import Enum


class GetChallengeDetailsView(str, Enum):
    DETAILS = "details"
    PICKS = "picks"

    def __str__(self) -> str:
        return str(self.value)
