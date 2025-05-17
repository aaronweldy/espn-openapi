from enum import Enum


class CategoryType(str, Enum):
    ATHLETE = "athlete"
    CONTRIBUTOR = "contributor"
    GUID = "guid"
    LEAGUE = "league"
    TEAM = "team"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
