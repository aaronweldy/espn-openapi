from enum import Enum


class NBATeamAbbreviation(str, Enum):
    ATL = "ATL"
    BKN = "BKN"
    BOS = "BOS"
    CHA = "CHA"
    CHI = "CHI"
    CLE = "CLE"
    DAL = "DAL"
    DEN = "DEN"
    DET = "DET"
    GS = "GS"
    HOU = "HOU"
    IND = "IND"
    LAC = "LAC"
    LAL = "LAL"
    MEM = "MEM"
    MIA = "MIA"
    MIL = "MIL"
    MIN = "MIN"
    NO = "NO"
    NY = "NY"
    OKC = "OKC"
    ORL = "ORL"
    PHI = "PHI"
    PHX = "PHX"
    POR = "POR"
    SA = "SA"
    SAC = "SAC"
    TOR = "TOR"
    UTAH = "UTAH"
    WSH = "WSH"

    def __str__(self) -> str:
        return str(self.value)
