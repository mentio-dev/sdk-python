from enum import StrEnum


class SlackChannelKind(StrEnum):
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
