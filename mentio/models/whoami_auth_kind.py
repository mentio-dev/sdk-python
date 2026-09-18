from enum import StrEnum


class WhoamiAuthKind(StrEnum):
    API_KEY = "api_key"
    OAUTH = "oauth"
    SESSION = "session"

    def __str__(self) -> str:
        return str(self.value)
