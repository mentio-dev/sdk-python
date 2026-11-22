from enum import StrEnum


class ListSearchesResponse200DataItemRange(StrEnum):
    VALUE_0 = "24h"
    VALUE_1 = "7d"
    VALUE_2 = "30d"
    VALUE_3 = "90d"
    VALUE_4 = "365d"

    def __str__(self) -> str:
        return str(self.value)
