from enum import StrEnum


class TrackedAccountPlatform(StrEnum):
    BLUESKY = "bluesky"
    GITHUB = "github"
    INSTAGRAM = "instagram"
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
