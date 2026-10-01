from enum import StrEnum


class KeywordSuggestionPatchPlatformsType0Item(StrEnum):
    BLUESKY = "bluesky"
    DEVTO = "devto"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    NEWS = "news"
    REDDIT = "reddit"
    STACKOVERFLOW = "stackoverflow"
    TIKTOK = "tiktok"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
