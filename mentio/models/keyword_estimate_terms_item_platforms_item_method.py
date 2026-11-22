from enum import StrEnum


class KeywordEstimateTermsItemPlatformsItemMethod(StrEnum):
    INDEX = "index"
    SAMPLE = "sample"

    def __str__(self) -> str:
        return str(self.value)
