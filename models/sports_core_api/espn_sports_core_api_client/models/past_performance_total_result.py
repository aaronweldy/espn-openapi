from enum import Enum


class PastPerformanceTotalResult(str, Enum):
    O = "O"
    P = "P"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
