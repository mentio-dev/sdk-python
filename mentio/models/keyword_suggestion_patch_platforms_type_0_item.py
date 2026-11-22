from enum import StrEnum


class KeywordSuggestionPatchPlatformsType0Item(StrEnum):
    BLUESKY = "bluesky"
    DEVTO = "devto"
    FACEBOOK = "facebook"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    MASTODON = "mastodon"
    NEWS = "news"
    PODCASTS = "podcasts"
    PRODUCTHUNT = "producthunt"
    REDDIT = "reddit"
    STACKOVERFLOW = "stackoverflow"
    SUBSTACK = "substack"
    THREADS = "threads"
    TIKTOK = "tiktok"
    WEB = "web"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
