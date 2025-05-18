from enum import Enum


class GetMLBTeamDetailsTeamIdOrAbbrev(str, Enum):
    ARI = "ARI"
    ATH = "ATH"
    ATL = "ATL"
    BAL = "BAL"
    BOS = "BOS"
    CHC = "CHC"
    CHW = "CHW"
    CIN = "CIN"
    CLE = "CLE"
    COL = "COL"
    DET = "DET"
    HOU = "HOU"
    KC = "KC"
    LAA = "LAA"
    LAD = "LAD"
    MIA = "MIA"
    MIL = "MIL"
    MIN = "MIN"
    NYM = "NYM"
    NYY = "NYY"
    PHI = "PHI"
    PIT = "PIT"
    SD = "SD"
    SEA = "SEA"
    SF = "SF"
    STL = "STL"
    TB = "TB"
    TEX = "TEX"
    TOR = "TOR"
    WSH = "WSH"

    def __str__(self) -> str:
        return str(self.value)
