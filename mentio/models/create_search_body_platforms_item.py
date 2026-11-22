from enum import StrEnum


class CreateSearchBodyPlatformsItem(StrEnum):
    BLUESKY = "bluesky"
    DEVTO = "devto"
    FACEBOOK = "facebook"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    NEWS = "news"
    PODCASTS = "podcasts"
    PRODUCTHUNT = "producthunt"
    REDDIT = "reddit"
    STACKOVERFLOW = "stackoverflow"
    SUBSTACK = "substack"
    TIKTOK = "tiktok"
    WEB = "web"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
