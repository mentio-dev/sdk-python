from enum import StrEnum


class UpdateSegmentBodyFilterPlatformsItem(StrEnum):
    BLUESKY = "bluesky"
    DEVTO = "devto"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    LINKEDIN = "linkedin"
    NEWS = "news"
    REDDIT = "reddit"
    STACKOVERFLOW = "stackoverflow"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
