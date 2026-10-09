from enum import StrEnum


class CreateKeywordBodyCapType0Per(StrEnum):
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
