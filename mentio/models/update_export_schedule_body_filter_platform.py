from enum import StrEnum


class UpdateExportScheduleBodyFilterPlatform(StrEnum):
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
    NEWS = "news"
    PODCASTS = "podcasts"
    PRODUCTHUNT = "producthunt"
    REDDIT = "reddit"
    RSS = "rss"
    STACKOVERFLOW = "stackoverflow"
    SUBSTACK = "substack"
    TIKTOK = "tiktok"
    TRUSTPILOT = "trustpilot"
    WEB = "web"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
