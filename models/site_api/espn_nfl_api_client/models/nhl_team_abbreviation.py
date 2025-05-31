from enum import Enum


class NHLTeamAbbreviation(str, Enum):
    ANA = "ANA"
    BOS = "BOS"
    BUF = "BUF"
    CAR = "CAR"
    CBJ = "CBJ"
    CGY = "CGY"
    CHI = "CHI"
    COL = "COL"
    DAL = "DAL"
    DET = "DET"
    EDM = "EDM"
    FLA = "FLA"
    LA = "LA"
    MIN = "MIN"
    MTL = "MTL"
    NJ = "NJ"
    NSH = "NSH"
    NYI = "NYI"
    NYR = "NYR"
    OTT = "OTT"
    PHI = "PHI"
    PIT = "PIT"
    SEA = "SEA"
    SJ = "SJ"
    STL = "STL"
    TB = "TB"
    TOR = "TOR"
    UTAH = "UTAH"
    VAN = "VAN"
    VGK = "VGK"
    WPG = "WPG"
    WSH = "WSH"

    def __str__(self) -> str:
        return str(self.value)
