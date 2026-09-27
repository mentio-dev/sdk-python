from enum import StrEnum


class ReviewsReportWindowBucket(StrEnum):
    DAY = "day"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
