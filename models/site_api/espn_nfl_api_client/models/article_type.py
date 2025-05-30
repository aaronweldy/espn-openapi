from enum import Enum


class ArticleType(str, Enum):
    HEADLINENEWS = "HeadlineNews"
    MEDIA = "Media"
    RECAP = "Recap"
    STORY = "Story"

    def __str__(self) -> str:
        return str(self.value)
