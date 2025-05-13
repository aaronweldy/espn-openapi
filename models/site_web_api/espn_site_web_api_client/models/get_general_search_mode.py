from enum import Enum


class GetGeneralSearchMode(str, Enum):
    FULL = "full"
    PREFIX = "prefix"

    def __str__(self) -> str:
        return str(self.value)
