from enum import StrEnum


class ListSearchesResponse200DataItemKind(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
