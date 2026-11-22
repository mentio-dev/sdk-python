from enum import StrEnum


class TeamsChannelKind(StrEnum):
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)
