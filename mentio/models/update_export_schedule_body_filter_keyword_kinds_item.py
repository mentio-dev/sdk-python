from enum import StrEnum


class UpdateExportScheduleBodyFilterKeywordKindsItem(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
