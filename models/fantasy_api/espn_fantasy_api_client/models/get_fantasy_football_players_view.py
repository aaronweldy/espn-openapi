from enum import Enum


class GetFantasyFootballPlayersView(str, Enum):
    ALLON = "allon"
    KONA_PLAYER_INFO = "kona_player_info"
    MBOXSCORE = "mBoxscore"
    MDRAFTDETAIL = "mDraftDetail"
    MLIVESCORING = "mLiveScoring"
    MMATCHUP = "mMatchup"
    MMATCHUPSCORE = "mMatchupScore"
    MROSTER = "mRoster"
    MSTANDINGS = "mStandings"
    MTEAM = "mTeam"
    PLAYER_WL = "player_wl"

    def __str__(self) -> str:
        return str(self.value)
