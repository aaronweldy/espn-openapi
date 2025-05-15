from enum import Enum


class GameEventAtVs(str, Enum):
    VALUE_1 = "@"
    VS = "vs"

    def __str__(self) -> str:
        return str(self.value)
