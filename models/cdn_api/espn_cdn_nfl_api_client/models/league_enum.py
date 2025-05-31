from enum import Enum


class LeagueEnum(str, Enum):
    ATP = "atp"
    BUNDESLIGA = "bundesliga"
    COLLEGE_BASEBALL = "college-baseball"
    COLLEGE_FOOTBALL = "college-football"
    EPL = "epl"
    EUROPA_LEAGUE = "europa-league"
    F1 = "f1"
    LALIGA = "laliga"
    LIGUE_1 = "ligue-1"
    LPGA = "lpga"
    MENS_COLLEGE_BASKETBALL = "mens-college-basketball"
    MLB = "mlb"
    MLS = "mls"
    NASCAR_PREMIER = "nascar-premier"
    NBA = "nba"
    NFL = "nfl"
    NHL = "nhl"
    OTHER = "other"
    PGA = "pga"
    SERIE_A = "serie-a"
    UCL = "ucl"
    WNBA = "wnba"
    WOMENS_COLLEGE_BASKETBALL = "womens-college-basketball"
    WTA = "wta"

    def __str__(self) -> str:
        return str(self.value)
