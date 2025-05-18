from enum import Enum


class SportEnum(str, Enum):
    BASEBALL = "baseball"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    GOLF = "golf"
    HOCKEY = "hockey"
    RACING = "racing"
    SOCCER = "soccer"
    TENNIS = "tennis"

    def __str__(self) -> str:
        return str(self.value)
