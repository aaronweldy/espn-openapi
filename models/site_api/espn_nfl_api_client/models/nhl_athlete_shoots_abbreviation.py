from enum import Enum


class NhlAthleteShootsAbbreviation(str, Enum):
    L = "L"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
