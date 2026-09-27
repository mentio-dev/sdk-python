from enum import StrEnum


class ListViewsResponse200DataItemFilterPlatformsItem(StrEnum):
    APPSTORE = "appstore"
    BLUESKY = "bluesky"
    DEVTO = "devto"
    GITHUB = "github"
    GOOGLEMAPS = "googlemaps"
    GOOGLEPLAY = "googleplay"
    HACKERNEWS = "hackernews"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    NEWS = "news"
    REDDIT = "reddit"
    STACKOVERFLOW = "stackoverflow"
    TIKTOK = "tiktok"
    TRUSTPILOT = "trustpilot"
    X = "x"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
