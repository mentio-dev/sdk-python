from enum import StrEnum


class ExportMentionsCsvPlatform(StrEnum):
    APPSTORE = "appstore"
    BLUESKY = "bluesky"
    DEVTO = "devto"
    GITHUB = "github"
    GOOGLEPLAY = "googleplay"
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
