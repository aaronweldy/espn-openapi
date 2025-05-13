from enum import Enum


class GetFantasyFootballTeamView(str, Enum):
    MMATCHUP = "mMatchup"
    MROSTER = "mRoster"
    MTEAM = "mTeam"

    def __str__(self) -> str:
        return str(self.value)
