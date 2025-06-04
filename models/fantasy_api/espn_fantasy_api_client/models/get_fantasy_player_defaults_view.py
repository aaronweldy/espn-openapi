from enum import Enum


class GetFantasyPlayerDefaultsView(str, Enum):
    KONA_PLAYER_INFO = "kona_player_info"

    def __str__(self) -> str:
        return str(self.value)
