from enum import StrEnum


class ReviewSourcePlatform(StrEnum):
    APPSTORE = "appstore"
    GOOGLEPLAY = "googleplay"

    def __str__(self) -> str:
        return str(self.value)
