from enum import Enum


class GameEventGameResult(str, Enum):
    L = "L"
    T = "T"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
