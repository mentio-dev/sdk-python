from enum import StrEnum


class ImportFeedsBodyFeedsItemAuthType1Type(StrEnum):
    HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)
