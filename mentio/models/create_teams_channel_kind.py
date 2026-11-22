from enum import StrEnum


class CreateTeamsChannelKind(StrEnum):
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)
