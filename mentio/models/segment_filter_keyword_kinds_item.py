from enum import StrEnum


class SegmentFilterKeywordKindsItem(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
