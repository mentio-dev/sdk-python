from enum import StrEnum


class MentionReviewType0AppPlatform(StrEnum):
    APPSTORE = "appstore"
    GOOGLEPLAY = "googleplay"

    def __str__(self) -> str:
        return str(self.value)
