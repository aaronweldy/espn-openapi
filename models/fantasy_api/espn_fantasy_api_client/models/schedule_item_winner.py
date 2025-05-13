from enum import Enum


class ScheduleItemWinner(str, Enum):
    AWAY = "AWAY"
    HOME = "HOME"
    UNDECIDED = "UNDECIDED"

    def __str__(self) -> str:
        return str(self.value)
