from enum import StrEnum


class KeywordHealthAiStatus(StrEnum):
    CACHED = "cached"
    GENERATED = "generated"
    OFF = "off"
    RATE_LIMITED = "rate_limited"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
