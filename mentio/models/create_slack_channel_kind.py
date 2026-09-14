from enum import StrEnum


class CreateSlackChannelKind(StrEnum):
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
