from enum import Enum


class NewsCategoryType(str, Enum):
    ATHLETE = "athlete"
    CONTRIBUTOR = "contributor"
    EDITORIALINDICATOR = "editorialindicator"
    EVENT = "event"
    GUID = "guid"
    LEAGUE = "league"
    PODCAST = "podcast"
    SERIES = "series"
    TEAM = "team"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
