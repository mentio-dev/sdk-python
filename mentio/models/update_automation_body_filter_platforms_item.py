from enum import StrEnum


class UpdateAutomationBodyFilterPlatformsItem(StrEnum):
    APPSTORE = "appstore"
    BLUESKY = "bluesky"
    DEVTO = "devto"
    FACEBOOK = "facebook"
    GITHUB = "github"
    GOOGLEMAPS = "googlemaps"
    GOOGLEPLAY = "googleplay"
    HACKERNEWS = "hackernews"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    MASTODON = "mastodon"
    NEWS = "news"
    PODCASTS = "podcasts"
    PRODUCTHUNT = "producthunt"
    REDDIT = "reddit"
    RSS = "rss"
    STACKOVERFLOW = "stackoverflow"
    SUBSTACK = "substack"
    THREADS = "threads"
    TIKTOK = "tiktok"
    TRUSTPILOT = "trustpilot"
    WEB = "web"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
