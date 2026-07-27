from enum import Enum


class NewsArticleType(str, Enum):
    COLUMNIST = "Columnist"
    ETICKET = "Eticket"
    HEADLINENEWS = "HeadlineNews"
    MEDIA = "Media"
    PREVIEW = "Preview"
    RECAP = "Recap"
    STORY = "Story"

    def __str__(self) -> str:
        return str(self.value)
