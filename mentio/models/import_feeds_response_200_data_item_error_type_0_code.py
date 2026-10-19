from enum import StrEnum


class ImportFeedsResponse200DataItemErrorType0Code(StrEnum):
    FEED_AUTH_NOT_CONFIGURED = "feed_auth_not_configured"
    FEED_LIMIT_REACHED = "feed_limit_reached"
    FEED_LOGIN_EXPIRED = "feed_login_expired"
    FEED_LOGIN_REQUIRED = "feed_login_required"
    FEED_UNREADABLE = "feed_unreadable"
    INTERNAL_ERROR = "internal_error"
    VALIDATION_ERROR = "validation_error"

    def __str__(self) -> str:
        return str(self.value)
