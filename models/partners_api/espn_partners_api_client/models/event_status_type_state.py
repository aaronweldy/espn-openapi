from enum import Enum


class EventStatusTypeState(str, Enum):
    IN = "in"
    POST = "post"
    PRE = "pre"

    def __str__(self) -> str:
        return str(self.value)
