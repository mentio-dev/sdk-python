from enum import StrEnum


class ListChannelDeliveriesResponse200DataItemKind(StrEnum):
    DIGEST = "digest"
    EVENT = "event"
    MENTION = "mention"

    def __str__(self) -> str:
        return str(self.value)
