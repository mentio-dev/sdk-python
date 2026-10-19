from enum import StrEnum


class ImportFeedsResponse200DataItemFeedType0HealthReason(StrEnum):
    BLOCKED = "blocked"
    LOGIN_EXPIRED = "login_expired"
    LOGIN_REQUIRED = "login_required"
    NOT_A_FEED = "not_a_feed"
    NOT_FOUND = "not_found"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
