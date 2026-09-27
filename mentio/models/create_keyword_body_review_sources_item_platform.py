from enum import StrEnum


class CreateKeywordBodyReviewSourcesItemPlatform(StrEnum):
    APPSTORE = "appstore"
    GOOGLEMAPS = "googlemaps"
    GOOGLEPLAY = "googleplay"
    TRUSTPILOT = "trustpilot"

    def __str__(self) -> str:
        return str(self.value)
