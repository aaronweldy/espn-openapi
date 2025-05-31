from enum import Enum


class WNBATeamAbbreviation(str, Enum):
    ATL = "ATL"
    CHI = "CHI"
    CONN = "CONN"
    DAL = "DAL"
    GS = "GS"
    IND = "IND"
    LA = "LA"
    LV = "LV"
    MIN = "MIN"
    NY = "NY"
    PHX = "PHX"
    SEA = "SEA"
    TOY = "TOY"
    WSH = "WSH"

    def __str__(self) -> str:
        return str(self.value)
