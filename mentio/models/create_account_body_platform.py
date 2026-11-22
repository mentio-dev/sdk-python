from enum import StrEnum


class CreateAccountBodyPlatform(StrEnum):
    BLUESKY = "bluesky"
    GITHUB = "github"
    INSTAGRAM = "instagram"
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
