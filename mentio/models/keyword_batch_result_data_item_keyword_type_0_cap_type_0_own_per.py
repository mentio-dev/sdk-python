from enum import StrEnum


class KeywordBatchResultDataItemKeywordType0CapType0OwnPer(StrEnum):
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
