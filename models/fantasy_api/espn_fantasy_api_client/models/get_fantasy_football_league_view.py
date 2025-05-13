from enum import Enum


class GetFantasyFootballLeagueView(str, Enum):
    MDRAFTDETAIL = "mDraftDetail"
    MMATCHUP = "mMatchup"
    MROSTER = "mRoster"
    MSETTINGS = "mSettings"
    MTEAM = "mTeam"

    def __str__(self) -> str:
        return str(self.value)
