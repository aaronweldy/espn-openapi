from enum import Enum


class NewsArticleType(str, Enum):
    HEADLINENEWS = "HeadlineNews"
    MEDIA = "Media"
    PREVIEW = "Preview"
    RECAP = "Recap"
    STORY = "Story"

    def __str__(self) -> str:
        return str(self.value)
