from enum import Enum


class GetRankingsLeague(str, Enum):
    COLLEGE_FOOTBALL = "college-football"
    MENS_COLLEGE_BASKETBALL = "mens-college-basketball"
    WOMENS_COLLEGE_BASKETBALL = "womens-college-basketball"

    def __str__(self) -> str:
        return str(self.value)
