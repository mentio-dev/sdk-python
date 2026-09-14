from enum import StrEnum


class UpdateSegmentBodyFilterNeverKeywordKindsItem(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
