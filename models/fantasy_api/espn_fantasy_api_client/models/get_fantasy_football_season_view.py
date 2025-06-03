from enum import Enum


class GetFantasyFootballSeasonView(str, Enum):
    PROTEAMSCHEDULES_WL = "proTeamSchedules_wl"

    def __str__(self) -> str:
        return str(self.value)
