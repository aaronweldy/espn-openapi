from enum import Enum


class MlbRosterAthleteBatsAbbreviation(str, Enum):
    B = "B"
    L = "L"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
