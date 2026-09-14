from enum import StrEnum


class ExportPeopleCsvKeywordKindsItem(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
