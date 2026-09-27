from enum import StrEnum


class UpdateKeywordBodyReviewSourcesItemPlatform(StrEnum):
    APPSTORE = "appstore"
    GOOGLEPLAY = "googleplay"

    def __str__(self) -> str:
        return str(self.value)
