from enum import StrEnum


class ExportDeliveryType0Kind(StrEnum):
    LINK = "link"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
