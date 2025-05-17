from enum import Enum


class NewsArticleType(str, Enum):
    HEADLINENEWS = "HeadlineNews"
    MEDIA = "Media"
    STORY = "Story"

    def __str__(self) -> str:
        return str(self.value)
