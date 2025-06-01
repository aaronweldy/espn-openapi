from enum import Enum


class FutureItemType(str, Enum):
    PLAYERPROP = "playerProp"
    TEAMPROP = "teamProp"
    WINCONFERENCE = "winConference"
    WINDIVISION = "winDivision"
    WINLEAGUE = "winLeague"

    def __str__(self) -> str:
        return str(self.value)
