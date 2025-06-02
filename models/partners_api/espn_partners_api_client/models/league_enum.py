from enum import Enum


class LeagueEnum(str, Enum):
    ATP = "atp"
    COLLEGE_BASEBALL = "college-baseball"
    COLLEGE_FOOTBALL = "college-football"
    ENG_1 = "eng.1"
    ESP_1 = "esp.1"
    F1 = "f1"
    FRA_1 = "fra.1"
    GER_1 = "ger.1"
    ITA_1 = "ita.1"
    LPGA = "lpga"
    MENS_COLLEGE_BASKETBALL = "mens-college-basketball"
    MLB = "mlb"
    NASCAR = "nascar"
    NBA = "nba"
    NFL = "nfl"
    NHL = "nhl"
    PGA = "pga"
    UEFA_CHAMPIONS = "uefa.champions"
    USA_1 = "usa.1"
    WNBA = "wnba"
    WOMENS_COLLEGE_BASKETBALL = "womens-college-basketball"
    WTA = "wta"

    def __str__(self) -> str:
        return str(self.value)
