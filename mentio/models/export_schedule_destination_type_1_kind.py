from enum import StrEnum


class ExportScheduleDestinationType1Kind(StrEnum):
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
