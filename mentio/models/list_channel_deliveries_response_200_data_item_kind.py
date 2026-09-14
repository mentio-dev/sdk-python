from enum import StrEnum


class ListChannelDeliveriesResponse200DataItemKind(StrEnum):
    DIGEST = "digest"
    MENTION = "mention"

    def __str__(self) -> str:
        return str(self.value)
